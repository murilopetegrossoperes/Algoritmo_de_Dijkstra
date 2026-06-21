# Cada chave é um vértice, e o valor é outro dicionário com {número/nome do vértice vizinho: peso_da_aresta}
grafo = {
    1: {2: 3, 3: 7, 4: 2},
    2: {1: 3, 4: 5, 5: 4},
    3: {1: 7, 4: 3},
    4: {1: 2, 2: 5, 3: 3, 6: 9},
    5: {2: 4},
    6: {4: 9}
}

def exibir_tabela_estado(distancia, predecessor, visitados):
    """Função auxiliar para renderizar o estado atual do algoritmo de forma organizada."""
    print(f"{'Vértice':^9} | {'Distância':^11} | {'Predecessor':^13} | {'Visitado':^10}")
    print("-" * 55)
    for v in sorted(distancia.keys()):
        dist_str = "∞" if distancia[v] == float('inf') else str(distancia[v])
        pred_str = f"V{predecessor[v]}" if predecessor[v] is not None else "-"
        vis_str = "Sim" if v in visitados else "Não"
        print(f"{f'V{v}':^9} | {dist_str:^11} | {pred_str:^13} | {vis_str:^10}")
    print("-" * 55)

def dijkstra_ilustrado(grafo, inicio):
    # 1. Inicialização das estruturas de dados
    vertices = list(grafo.keys())
    distancia = {v: float('inf') for v in vertices}
    predecessor = {v: None for v in vertices}
    visitados = set()

    # A distância do vértice inicial para ele mesmo é sempre 0
    distancia[inicio] = 0

    print("=================== ESTADO INICIAL ===================")
    exibir_tabela_estado(distancia, predecessor, visitados)

    passo = 1
    while len(visitados) < len(vertices):
        # 2. Busca pelo vértice não visitado com a menor distância atual
        u = None
        menor_distancia = float('inf')

        for v in vertices:
            if v not in visitados and distancia[v] < menor_distancia:
                menor_distancia = distancia[v]
                u = v

        # Se u for None, os vértices restantes são inacessíveis (fim do algoritmo)
        if u is None:
            break

        # Marcar o vértice escolhido como visitado
        visitados.add(u)

        print(f"\n[PASSO {passo}] -> Escolhendo o Vértice V{u} (Menor distância provisória: {distancia[u]})")

        # 3. Atualização (relaxamento) das distâncias dos vizinhos de 'u'
        print("Verificando vizinhos:")
        atualizou_algo = False
        for vizinho, peso in grafo[u].items():
            if vizinho not in visitados:
                nova_distancia = distancia[u] + peso

                # Se encontramos um caminho mais curto, atualizamos
                if nova_distancia < distancia[vizinho]:
                    print(f"  • Vizinho V{vizinho}: caminho antigo {distancia[vizinho]} -> novo caminho {nova_distancia} (via V{u})")
                    distancia[vizinho] = nova_distancia
                    predecessor[vizinho] = u
                    atualizou_algo = True
                else:
                    print(f"  • Vizinho V{vizinho}: caminho mantido {distancia[vizinho]} (novo proposto seria {nova_distancia})")

        if not atualizou_algo:
            print("  • Nenhum vizinho pendente recebeu um caminho menor.")

        print(f"\n================ TABELA APÓS PASSO {passo} ================")
        exibir_tabela_estado(distancia, predecessor, visitados)
        passo += 1

    return distancia, predecessor

def mostrar_caminhos_finais(distancia, predecessor, inicio):
    """Reconstrói e exibe os caminhos formados de trás para frente."""
    print("\n================== CAMINHOS FINAIS ==================")
    for v in sorted(distancia.keys()):
        caminho = []
        atual = v
        while atual is not None:
            caminho.append(f"V{atual}")
            atual = predecessor[atual]
        caminho.reverse()
        caminho_formatado = " → ".join(caminho)
        print(f"Destino: V{v} | Custo Total: {distancia[v]:<2} | Caminho: {caminho_formatado}")
    print("=====================================================")

#Escolhe o vértice inicial
vertice = int(input("Digite o número do vértice inicial: "))

# Executa o algoritmo iniciando no vértice selecionado
distancias_finais, predecessores_finais = dijkstra_ilustrado(grafo, inicio=vertice)
mostrar_caminhos_finais(distancias_finais, predecessores_finais, inicio=vertice)
