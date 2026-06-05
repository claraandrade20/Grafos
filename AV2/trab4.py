from collections import deque

def bfs_menor_rota(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None

    fila = deque([[origem]])

    visitados = set([origem])

    while fila:
        caminho = fila.popleft()

        vertice_atual = caminho[-1]

        if vertice_atual == destino:
            return caminho

        for vizinho in grafo.get(vertice_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return None

grafo_logistica = {
    "Manaus": ["Belém", "Fortaleza"],
    "Belém": ["Manaus", "Recife", "Fortaleza"],
    "Fortaleza": ["Manaus", "Belém", "Recife", "Salvador"],
    "Recife": ["Belém", "Fortaleza", "Salvador", "BH"],
    "Salvador": ["Fortaleza", "Recife", "BH", "Brasília"],
    "BH": ["Recife", "Salvador", "RJ", "Brasília", "SP"],
    "Brasília": ["Salvador", "BH", "SP", "Goiânia"],
    "RJ": ["BH", "SP"],
    "SP": ["BH", "Brasília", "RJ", "Curitiba", "Goiânia"],
    "Goiânia": ["Brasília", "SP", "Curitiba"],
    "Curitiba": ["SP", "Goiânia", "Porto Alegre"],
    "Porto Alegre": ["Curitiba"]
}

testes = [
    ("Manaus", "Porto Alegre"),
    ("Belém", "Goiânia"),
    ("Fortaleza", "RJ")
]

print("--- SISTEMA DE ROTAS DE LOGÍSTICA ---\n")

for origem, destino in testes:
    print(f"Buscando rota: {origem} -> {destino}")
    rota = bfs_menor_rota(grafo_logistica, origem, destino)

    if rota:
        num_paradas = len(rota) - 1
        print(f"Caminho encontrado: {' -> '.join(rota)}")
        print(f"Número de paradas: {num_paradas}\n")
    else:
        print(f"Não existe rota disponível entre {origem} e {destino}.\n")