grafo = {
    "AC": ["AM", "RO"],
    "AL": ["BA", "PE", "SE"],
    "AM": ["AC", "RO", "MT", "PA", "RR"],
    "AP": ["PA"],
    "BA": ["AL", "SE", "PE", "PI", "TO", "GO", "MG", "ES"],
    "CE": ["RN", "PB", "PE", "PI"],
    "DF": ["GO", "MG"],
    "ES": ["BA", "MG", "RJ"],
    "GO": ["TO", "BA", "MG", "MS", "MT", "DF"],
    "MA": ["PA", "TO", "PI"],
    "MG": ["BA", "GO", "SP", "RJ", "DF", "ES"],
    "MS": ["MT", "GO", "SP", "PR"],
    "MT": ["RO", "AM", "PA", "TO", "GO", "MS"],
    "PA": ["AP", "MA", "TO", "MT", "AM", "RR"],
    "PB": ["RN", "CE", "PE"],
    "PE": ["PB", "CE", "PI", "BA", "AL"],
    "PI": ["MA", "TO", "BA", "PE", "CE"],
    "PR": ["SP", "MS", "SC"],
    "RJ": ["SP", "MG", "ES"],
    "RN": ["CE", "PB"],
    "RO": ["AC", "AM", "MT"],
    "RR": ["AM", "PA"],
    "RS": ["SC"],
    "SC": ["PR", "RS"],
    "SE": ["BA", "AL"],
    "SP": ["MG", "RJ", "MS", "PR"],
    "TO": ["PA", "MA", "PI", "BA", "GO", "MT"]
}


def vertice_maior_grau():
    maior_grau = float('-inf')
    estado_maior = None

    for estado in grafo:
        grau = len(grafo[estado])
        if grau > maior_grau:
            maior_grau = grau
            estado_maior = estado

    print(f"\nO estado com maior numero de vizinhos é {estado_maior}")
    print(f"Grau: {maior_grau}")
    print("Estados vizinhos:")
    for vizinho in grafo[estado_maior]:
        print(vizinho)


def vertice_menor_grau():
    menor_grau = float('inf')
    estados_menor = []

    for estado in grafo:
        grau = len(grafo[estado])
        if grau < menor_grau:
            menor_grau = grau

    for estado in grafo:
        if len(grafo[estado]) == menor_grau:
            estados_menor.append(estado)

    print(f"\nEstados com menor numero de vizinhos:")
    print(f"Numero de vizinhos: {menor_grau}\n")

    for estado in estados_menor:
        print(f"{estado} faz divisa com:")
        for vizinho in grafo[estado]:
            print(f"{vizinho}")
        print()


def desenhar_grafo():
    print("\n" + "="*60)
    print("MAPA DO BRASIL - GRAFO DE ESTADOS")
    print("="*60)
    print("\nTodos os estados e suas conexoes:\n")
    
    estados_ordenados = sorted(grafo.keys())
    
    for estado in estados_ordenados:
        vizinhos = sorted(grafo[estado])
        grau = len(vizinhos)
        print(f"{estado} (grau {grau}) -> {', '.join(vizinhos)}")
    
    print("\n" + "="*60)
    print(f"Total de estados (vertices): {len(grafo)}")
    
    total_arestas = sum(len(vizinhos) for vizinhos in grafo.values()) // 2
    print(f"Total de conexoes (arestas): {total_arestas}")
    print("="*60 + "\n")

def main():
    desenhar_grafo()
    vertice_maior_grau()
    vertice_menor_grau()

if __name__ == "__main__":
    main()