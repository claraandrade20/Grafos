grafo1 = {
    0: [1, 2, 3], 
    1: [0, 4, 5], 
    2: [0, 5, 6], 
    3: [0, 6, 7],
    4: [1, 8], 
    5: [1, 2, 9], 
    6: [2, 3, 9, 10], 
    7: [3, 10],
    8: [4, 11], 
    9: [5, 6, 11, 12], 
    10: [6, 7, 12, 13],
    11: [8, 14, 9], 
    12: [9, 10, 14], 
    13: [10, 14], 
    14: [11, 12, 13]
}

grafo2 = {
    0: [1, 2], 
    1: [0, 3, 4], 
    2: [0, 4, 5], 
    3: [1, 6], 
    4: [1, 2, 7, 8], 
    5: [2, 8, 9], 
    6: [3, 10], 
    7: [4, 10, 11], 
    8: [4, 5, 11, 12], 
    9: [5, 12], 
    10: [6, 7, 13], 
    11: [7, 8, 13, 14], 
    12: [8, 9, 14, 15], 
    13: [10, 11, 16], 
    14: [11, 12, 16, 17], 
    15: [12, 17], 
    16: [13, 14, 17], 
    17: [14, 15, 16]
}


def dfs_recursiva(grafo, atual, destino, visitados, caminho_atual):
    visitados.add(atual)
    caminho_atual.append(atual)

    if atual == destino:
        return caminho_atual

    for vizinho in grafo[atual]:
        if vizinho not in visitados:
            resultado = dfs_recursiva(grafo, vizinho, destino, visitados, caminho_atual)
            if resultado:
                return resultado 

    caminho_atual.pop()
    return None

def resolver_dfs_iterativa(grafo, origem, destino):
    pilha = [origem]
    visitados = set()
    predecessor = {origem: None}
    encontrado = False

    while pilha:
        atual = pilha.pop()

        if atual == destino:
            encontrado = True
            break

        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    if vizinho not in predecessor:
                        predecessor[vizinho] = atual
                    pilha.append(vizinho)

    if encontrado:
        caminho = []
        passo = destino
        while passo is not None:
            caminho.append(passo)
            passo = predecessor[passo]
        caminho.reverse()
        return caminho;
    return None

print("Grafo 1 (Recursivo)")
resultado1 = dfs_recursiva(grafo1, 0, 14, set(), [])
if resultado1:
    print(f"Caminho: {' -> '.join(map(str, resultado1))}")
    print(f"Distância: {len(resultado1) - 1}")
else:
    print("SEM CAMINHO")

print("\nGrafo 2 (Iterativo)")
resultado2 = resolver_dfs_iterativa(grafo2, 3, 15)
if resultado2:
    print(f"Caminho: {' -> '.join(map(str, resultado2))}")
    print(f"Distância: {len(resultado2) - 1}")
else:
    print("SEM CAMINHO")