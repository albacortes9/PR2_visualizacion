import pandas as pd
import plotly.graph_objects as go

# Cargar el dataset
df = pd.read_csv("CO2_emissions.csv")

# Agrupar por país y sector
df_grouped = df.groupby(['country', 'sector'], as_index=False)['value'].sum()

# Crear nodos únicos
all_nodes = list(pd.concat([df_grouped['country'], df_grouped['sector']]).unique())
node_indices = {node: i for i, node in enumerate(all_nodes)}

# Mapear source con país, target con sector y valor
source = df_grouped['country'].map(node_indices)
target = df_grouped['sector'].map(node_indices)
value = df_grouped['value']

# Crear Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_nodes,
        color="green"
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(
    title_text="Sankey Diagram de emisiones de CO2 por país y sector",
    font_size=12,
    width=900,
    height=600
)

fig.show()
