import random
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import osmnx as ox
import networkx as nx
from collections import deque


def configurar_cache_osm():
    cache_dir = Path(__file__).resolve().parent / 'cache'
    cache_dir.mkdir(exist_ok=True)
    ox.settings.use_cache = True
    ox.settings.cache_folder = str(cache_dir)

def bfs(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return None
    fila = deque([[origem]])
    visitados = {origem}
    
    while fila:
        caminho = fila.popleft()
        vertice_atual = caminho[-1]
        if vertice_atual == destino:
            return caminho
        for vizinho in grafo.get(vertice_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
    return None

def dijkstra(grafo, inicio):
    if not grafo or inicio not in grafo:
        return {}, {}
    
    dist = {v: float('inf') for v in grafo}
    anterior = {v: None for v in grafo}
    dist[inicio] = 0
    nao_visitados = set(grafo.keys())
    
    while nao_visitados:
        vertice_atual = min(nao_visitados, key=lambda v: dist[v])
        if dist[vertice_atual] == float('inf'):
            break
        nao_visitados.remove(vertice_atual)
        
        for vizinho, peso in grafo[vertice_atual]:
            if vizinho in nao_visitados:
                nova_dist = dist[vertice_atual] + peso
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    anterior[vizinho] = vertice_atual
    return dist, anterior

def reconstruir_caminho(anterior, destino):
    if not anterior.get(destino) and destino not in anterior:
        return None
    caminho, atual = [], destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = anterior[atual]
    return caminho if caminho and caminho[0] != destino else None

def estatisticas_grafo(grafo):
    graus = [len(grafo[v]) for v in grafo]
    vertice_importante = max(grafo, key=lambda v: len(grafo[v]))
    num_arestas = sum(graus) // 2
    possui_ciclos = len(grafo) > 0 and num_arestas > (len(grafo) - 1)
    
    return {
        'num_vertices': len(grafo),
        'num_arestas': num_arestas,
        'grau_medio': sum(graus) / len(grafo),
        'grau_maximo': max(graus),
        'grau_minimo': min(graus),
        'vertice_importante': vertice_importante,
        'possui_ciclos': possui_ciclos
    }

def analisar_conectividade(grafo, origem, destino):
    return bfs(grafo, origem, destino) is not None

def extrair_dados_osm(ponto_inicial, ponto_final, distancia_raio=4000):
    print(f"   → Baixando mapa de Fortaleza (raio de {distancia_raio}m)...")
    lat_centro = (ponto_inicial[0] + ponto_final[0]) / 2
    lon_centro = (ponto_inicial[1] + ponto_final[1]) / 2
    
    try:
        G = ox.graph_from_point((lat_centro, lon_centro), dist=distancia_raio, 
                                network_type='drive', simplify=True)
    except Exception as e:
        print(f"Erro ao baixar: {e}")
        return None
    
    origem_id = ox.distance.nearest_nodes(G, ponto_inicial[1], ponto_inicial[0])
    destino_id = ox.distance.nearest_nodes(G, ponto_final[1], ponto_final[0])
    
    grafo_bfs, grafo_dijkstra, posicoes, pesos_arestas = {}, {}, {}, {}
    node_mapping = {node: idx for idx, node in enumerate(G.nodes())}
    
    tipos_terreno = {'terra': 2, 'agua': 10, 'deserto': lambda: random.randint(20, 25), 'fogo': lambda: random.randint(50, 100)}
    
    for node in G.nodes():
        idx = node_mapping[node]
        grafo_bfs[idx], grafo_dijkstra[idx] = [], []
        posicoes[idx] = (G.nodes[node]['x'], G.nodes[node]['y'])

    for u, v, data in G.edges(data=True):
        u_idx, v_idx = node_mapping[u], node_mapping[v]
        bioma = random.choices(['terra', 'agua', 'deserto', 'fogo'], weights=[50, 25, 15, 10])[0]
        peso = tipos_terreno[bioma]() if callable(tipos_terreno[bioma]) else tipos_terreno[bioma]
        
        grafo_bfs[u_idx].append(v_idx)
        grafo_dijkstra[u_idx].append((v_idx, peso))
        pesos_arestas[(u_idx, v_idx)] = peso

    return grafo_bfs, grafo_dijkstra, posicoes, pesos_arestas, node_mapping[origem_id], node_mapping[destino_id]


def imprimir_resultados(stats, caminho_bfs, caminho_dijkstra, pesos_arestas, origem, destino):
    custo_bfs = sum(pesos_arestas.get((caminho_bfs[i], caminho_bfs[i+1]), 2) for i in range(len(caminho_bfs)-1))
    custo_dijkstra = sum(pesos_arestas.get((caminho_dijkstra[i], caminho_dijkstra[i+1]), 2) for i in range(len(caminho_dijkstra)-1))
    economia = ((custo_bfs - custo_dijkstra) / custo_bfs * 100) if custo_bfs > 0 else 0

    print("Sistema de Labirinto em Fortaleza com Biomas".center(70))
    print(f"\nGRAFO: {stats['num_vertices']} vértices | {stats['num_arestas']} arestas")
    print(f"Vértice mais importante (Maior grau): {stats['vertice_importante']}")
    print(f"Presença de Ciclos detectada: {'Sim' if stats['possui_ciclos'] else 'Não'}")
    print(f"ROTA: Residência ({origem}) → UNIFOR ({destino})")
    
    print(f"\nBFS (Caminho mais rápido):")
    print(f" > Nós percorridos: {len(caminho_bfs)}")
    print(f" > Custo total: {custo_bfs}")
    
    print(f"\nDIJKSTRA (Caminho mais seguro):")
    print(f" > Nós percorridos: {len(caminho_dijkstra)}")
    print(f" > Custo total: {custo_dijkstra}")
    
    print(f"\nCOMPARAÇÃO:")
    print(f" > Economia de custo com Dijkstra: {economia:.1f}%")
    print(f" > Diferença de nós: {len(caminho_dijkstra) - len(caminho_bfs)} nós extras")
    
    return custo_bfs, custo_dijkstra

def visualizar(grafo_bfs, posicoes, pesos_arestas, caminho_bfs, caminho_dijkstra, c_bfs, c_dijkstra, origem, destino):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    cores = {2: '#90EE90', 10: '#4682B4', 20: '#D2691E', 50: '#FF4500'}
    
    for ax, caminho, cor_linha, titulo, custo, num_nos in [
        (ax1, caminho_bfs, 'blue', f'BFS - {len(caminho_bfs)} nós | Custo: {c_bfs}', c_bfs, len(caminho_bfs)),
        (ax2, caminho_dijkstra, 'purple', f'Dijkstra - {len(caminho_dijkstra)} nós | Custo: {c_dijkstra}', c_dijkstra, len(caminho_dijkstra))
    ]:
        ax.set_title(titulo, fontweight='bold')
        for u in grafo_bfs:
            for v in grafo_bfs[u]:
                x, y = zip(posicoes[u], posicoes[v])
                peso = pesos_arestas.get((u, v), 2)
                ax.plot(x, y, color=cores.get(peso, '#CCCCCC') if peso < 20 else cores[20], alpha=0.3, linewidth=1)
        
        xc, yc = zip(*[posicoes[n] for n in caminho])
        ax.plot(xc, yc, color=cor_linha, linewidth=3, alpha=0.8)
        ax.scatter(*posicoes[origem], c='green', s=100, label='Origem', zorder=5)
        ax.scatter(*posicoes[destino], c='red', s=100, label='Destino', zorder=5)

    plt.tight_layout()
    plt.savefig('analise_grafos_unifor.png')
    plt.show()

def main():
    configurar_cache_osm()
    residencia = (-3.7590, -38.5837) 
    unifor = (-3.7733, -38.4760)  
    
    dados = extrair_dados_osm(residencia, unifor)
    if not dados: return
    
    g_bfs, g_dijkstra, pos, pesos, start, end = dados
    
    if analisar_conectividade(g_bfs, start, end):
        stats = estatisticas_grafo(g_bfs)
        c_bfs = bfs(g_bfs, start, end)
        dist, ant = dijkstra(g_dijkstra, start)
        c_dijkstra = reconstruir_caminho(ant, end)
        
        custo_b, custo_d = imprimir_resultados(stats, c_bfs, c_dijkstra, pesos, start, end)
        visualizar(g_bfs, pos, pesos, c_bfs, c_dijkstra, custo_b, custo_d, start, end)
    else:
        print("Erro: Caminho não encontrado entre os pontos.")

if __name__ == "__main__":
    main()