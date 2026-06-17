import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx

# 1. Definição do grafo
grafo_dados = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['4', '5'],
    '4': ['6'],
    '5': ['4'],
    '6': []
}

G = nx.DiGraph()
for no, vizinhos in grafo_dados.items():
    for vizinho in vizinhos:
        G.add_edge(no, vizinho)

# 2. Coordenadas (x, y) das camadas
posicoes = {
    '1': (0, 3),  # Camada 0
    '2': (-1, 2),
    '3': (1, 2),  # Camada 1
    '4': (-0.5, 1),
    '5': (1.5, 1),  # Camada 2
    '6': (0, 0)  # Camada 3
}

# 3. Definição de cores por proximidade (Dicionário de mapeamento)
cores_legenda = {
    'Não visitado': '#FFFFFF',
    'Na fila / pilha': '#808080',
    'Visitado': '#000000'
}

cores_nos = {
    '1': '#000000',
    '2': '#808080',
    '3': '#FFFFFF',
    '4': '#FFFFFF',
    '5': '#FFFFFF',
    '6': '#FFFFFF'
}
lista_cores = [cores_nos[no] for no in G.nodes()]

# 4. Configuração da área de plotagem (Aumentada para acomodar o texto lateral)
fig, ax = plt.subplots(figsize=(11, 7))
plt.title(
    'Busca em Profundidade (DFS) - Rastreamento Completo',
    fontsize=14,
    fontweight='bold',
    pad=20,
)

# Desenhar nós, rótulos e arestas curvas
nx.draw_networkx_nodes(
    G,
    posicoes,
    node_size=1200,
    node_color=lista_cores,
    edgecolors='black',
    linewidths=1.5,
    ax=ax,
)
nx.draw_networkx_labels(
    G, posicoes, font_size=12, font_weight='bold', font_color='black', ax=ax
)
nx.draw_networkx_edges(
    G,
    posicoes,
    arrowstyle='->',
    arrowsize=25,
    edge_color='#7f8c8d',
    width=2,
    connectionstyle='arc3,rad=0.1',
    ax=ax,
)

# 5. Criação Dinâmica da Legenda de Cores
patches_legenda = [
    mpatches.Patch(color=cor, label=desc) for desc, cor in cores_legenda.items()
]
ax.legend(
    handles=patches_legenda,
    loc='upper left',
    title='Camadas da DFS',
    title_fontproperties={'weight': 'bold'},
    frameon=True,
    shadow=True,
    facecolor='#f8f9fa',
)

# 6. Caixa de Texto Lateral: Histórico da Fila (FIFO) e Resultado
texto_fila = (
    "Vertice 1 processado. Desempilha 2, empilha vizinhos 4"

)

# Inserindo o quadro de texto na lateral direita do gráfico usando coordenadas da figura
plt.gcf().text(
    0.68,
    0.35,
    texto_fila,
    fontsize=10.5,
    family='monospace',
    verticalalignment='center',
    bbox=dict(
        boxstyle='round,pad=0.6',
        facecolor='#fcfcfc',
        edgecolor='#bdc3c7',
        lw=1.5,
    ),
)

# Ajuste de margens para o texto não cortar na direita
plt.subplots_adjust(right=0.65)
plt.axis('off')
plt.show()
