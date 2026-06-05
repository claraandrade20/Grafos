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
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [1, 2, 6]
}


def verificar_dirac(grafo):
    n = len(grafo)
    
    if n < 3:
        return False
    
    for i in grafo:
        grau = len(grafo[i])
        
        if grau < n / 2:
            return False
    
    return True


def verificar_ore(grafo):
    n = len(grafo)
    
    if n < 3:
        return False
    
    vertices = list(grafo.keys())
    
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            u, v = vertices[i], vertices[j]
            if v not in grafo[u] and len(grafo[u]) + len(grafo[v]) < n:
                return False
    
    return True


def verificar_bondy(grafo):
    n = len(grafo)
    
    if n < 3:
        return False
    
    novo_grafo = {}
    for i in grafo:
        novo_grafo[i] = grafo[i].copy()
    
    vertices = list(grafo.keys())
    mudou = True
    while mudou:
        mudou = False
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                u, v = vertices[i], vertices[j]
                if v not in novo_grafo[u] and len(novo_grafo[u]) + len(novo_grafo[v]) >= n:
                    novo_grafo[u].append(v)
                    novo_grafo[v].append(u)
                    mudou = True
    
    for i in grafo:
        if len(novo_grafo[i]) != n - 1:
            return False
    
    return True


def exibir_analise(grafo, numero):
    n = len(grafo)
    print(f"Grafo {numero}")
    
    graus = [len(grafo[i]) for i in grafo]
    print(f"Numero de vertices: {n}")
    print(f"Grau minimo: {min(graus)}, Grau maximo: {max(graus)}")
    
    dirac = verificar_dirac(grafo)
    ore = verificar_ore(grafo)
    bondy = verificar_bondy(grafo)
    
    print(f"Teorema de Dirac:          {'SIM' if dirac else 'NAO'}")
    print(f"Teorema de Ore:            {'SIM' if ore else 'NAO'}")
    print(f"Teorema de Bondy & Chvatal: {'SIM' if bondy else 'NAO'}")
    print()


exibir_analise(grafo1, 1)
exibir_analise(grafo2, 2)
exibir_analise(grafo3, 3)
exibir_analise(grafo4, 4)