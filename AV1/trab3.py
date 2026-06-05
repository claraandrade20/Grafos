grafo1 = {
    1: [2, 5, 6, 7],
    2: [1, 3, 4, 7],
    3: [2, 4, 5, 7],
    4: [2, 3, 5, 6],
    5: [1, 3, 4, 6],
    6: [1, 4, 5, 7],
    7: [1, 2, 3, 6]
}

grafo2 = {
    1: [2, 5, 6, 7],
    2: [1, 3, 4, 7],
    3: [2, 4, 5, 7],
    4: [2, 3, 5],
    5: [1, 3, 4, 6],
    6: [1, 5, 7],
    7: [1, 2, 3, 6]
}

grafo3 = {
    1: [2, 6, 7],
    2: [1, 3, 4, 7],
    3: [2, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [1, 5, 7],
    7: [1, 2, 6]
}

grafo4 = {
    1: [2, 7],
    2: [1, 3, 4, 7],
    3: [2, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [1, 2, 6]
}


def classificar_euleriano(grafo, numero):
    print(f"Grafo {numero}")

    vertices_impares = [v for v in grafo if len(grafo[v]) % 2 != 0]
    qtd_impares = len(vertices_impares)

    graus = {v: len(grafo[v]) for v in grafo}
    for v, g in graus.items():
        print(f"  Vertice {v}: grau {g} ({'impar' if g % 2 != 0 else 'par'})")

    if qtd_impares == 0:
        print("Classificacao: Euleriano (todos os graus sao pares -> existe circuito Euleriano)")
    elif qtd_impares == 2:
        print(f"Classificacao: Semi-Euleriano (vertices de grau impar: {vertices_impares} -> existe caminho Euleriano)")
    else:
        print(f"Classificacao: Nao Euleriano ({qtd_impares} vertices com grau impar)")
    print()


classificar_euleriano(grafo1, 1)
classificar_euleriano(grafo2, 2)
classificar_euleriano(grafo3, 3)
classificar_euleriano(grafo4, 4)

