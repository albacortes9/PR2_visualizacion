import seaborn as sns
import matplotlib.pyplot as plt
import ptitprince as pt

# Cargar dataset de penguins
df = sns.load_dataset("penguins")

# Eliminar filas con datos nulos
df = df.dropna(subset=["species", "flipper_length_mm"])

# Configurar figura
plt.figure(figsize=(10,6))
ax = plt.subplot()

# Crear raincloud plot
pt.RainCloud(
    x = "species",               # variable categórica
    y = "flipper_length_mm",     # variable numérica
    data = df,
    palette = "Set2",
    width_viol = 0.6,            # ancho del violín
    ax = ax,
    orient = "v"                 # vertical
)

# Títulos y etiquetas
plt.title("Raincloud Plot: Longitud de aleta por especie de pingüino", fontsize=14)
plt.xlabel("Especie")
plt.ylabel("Longitud de aleta (mm)")
plt.show()
