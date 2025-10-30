import pandas as pd
import matplotlib.pyplot as plt

dtype_spec = {
    "tconst": "string",
    "titleType": "category",
    "primaryTitle": "string",
    "originalTitle": "string",
    "isAdult": "Int64",
    "startYear": "string",      # primero como string, luego convertimos a numérico
    "endYear": "string",
    "runtimeMinutes": "string",
    "genres": "string"
}

df = pd.read_csv(
    "title.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    dtype=dtype_spec
)
# Filtrar solo películas no adultas
df = df[(df["titleType"] == "movie") & (df["isAdult"] == 0)]

# Eliminar filas sin año o sin género
df = df.dropna(subset=["startYear", "genres"])

# Convertir el año a numérico
df["startYear"] = pd.to_numeric(df["startYear"], errors="coerce")
df = df.dropna(subset=["startYear"])

# Tomar solo el primer género
df["genre_main"] = df["genres"].str.split(",").str[0]

# Filtrar por rango de año
df = df[(df["startYear"] >= 1920) & (df["startYear"] <= 2024)]

# Agrupar por año y género
counts = df.groupby(["startYear", "genre_main"]).size().reset_index(name="count")

# Pivotear los datos: géneros en columnas, años en filas
pivot = counts.pivot(index="startYear", columns="genre_main", values="count").fillna(0)

# Ordenar géneros por volumen total
pivot = pivot[pivot.sum().sort_values(ascending=False).index[:10]]  # top 10 géneros

fig, ax = plt.subplots(figsize=(12,6))
ax.stackplot(pivot.index, pivot.T, baseline='wiggle', labels=pivot.columns)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
ax.set_title("Stream Graph IMDb – Películas por género", fontsize=14)
ax.set_xlabel("Año")
ax.set_ylabel("Número relativo de películas")
plt.tight_layout()
plt.show()