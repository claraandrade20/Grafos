grafo = {
    'A': [('B', 4), ('C', 2), ('D', 7)],
    'B': [('C', 1), ('E', 3), ('F', 6)],
    'C': [('D', 4), ('F', 8), ('G', 5)],
    'D': [('G', 2), ('H', 3)],
    'E': [('F', 2), ('I', 5)],
    'F': [('I', 1), ('J', 4)],
    'G': [('J', 3), ('K', 7)],
    'H': [('K', 4), ('L', 6)],
    'I': [('M', 3)],
    'J': [('K', 2), ('M', 4), ('N', 6)],
    'K': [('L', 3), ('O', 8)],
    'L': [('O', 2)],
    'M': [('N', 1)],
    'N': [('O', 4)],
    'O': [],
    'P': [('Q', 3), ('R', 9)],
    'Q': [('R', 5)],
    'R': [('S', 2)],
    'S': [('T', 4)],
    'T': [('P', 6)]
}


def dijkstra(grafo, inicio):
    if not grafo:
        return {}, {}

    dist = {}
    anterior = {}
    nao_visitados = set()

    for vertice in grafo:
        dist[vertice] = float('inf')
        anterior[vertice] = None
        nao_visitados.add(vertice)

    if inicio not in grafo:
        return dist, anterior

    dist[inicio] = 0

    while nao_visitados:
        vertice_atual = None
        menor_dist = float('inf')

        for vertice in nao_visitados:
            if dist[vertice] < menor_dist:
                menor_dist = dist[vertice]
                vertice_atual = vertice

        if vertice_atual is None or dist[vertice_atual] == float('inf'):
            break

        nao_visitados.remove(vertice_atual)

        for vizinho, peso in grafo[vertice_atual]:
            if vizinho in nao_visitados:
                nova_dist = dist[vertice_atual] + peso

                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    anterior[vizinho] = vertice_atual

    return dist, anterior


def reconstruir_caminho(anterior, inicio, destino):
    if inicio not in anterior or destino not in anterior:
        return []

    if inicio == destino:
        return [inicio]

    caminho = []
    atual = destino

    while atual is not None and atual in anterior:
        caminho.append(atual)
        atual = anterior[atual]

    caminho = list(reversed(caminho))

    if not caminho or caminho[0] != inicio:
        return []

    return caminho



fonte = 'A'
dist, anterior = dijkstra(grafo, fonte)

print("\nResultados dos caminhos mínimos:\n")
print(f"{'Vértice':<10} {'Distância':<15} {'Caminho Mínimo':<40}")


for vertice in sorted(grafo.keys()):
    caminho = reconstruir_caminho(anterior, fonte, vertice)

    if vertice not in dist or dist[vertice] == float('inf') or not caminho:
        print(f"{vertice:<10} {'∞':<15} {'(não alcançável)':<40}")
    else:
        caminho_str = " -> ".join(caminho)
        print(f"{vertice:<10} {dist[vertice]:<15} {caminho_str:<40}")