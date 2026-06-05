# Sistema de Navegação e Otimização de Percurso em Fortaleza

**Aluno:** Maria Clara Andrade Gomes  
**Matrícula:** 2413526  
**Disciplina:** Teoria dos Grafos

---

## Descrição

Este projeto modela um problema de navegação urbana como grafo ponderado usando dados reais do OpenStreetMap. O programa extrai a malha viária da região entre a residência e a UNIFOR, aplica pesos artificiais nas ruas para simular biomas de risco e compara duas estratégias de busca:

1. BFS para obter um caminho com menor número de nós.
2. Dijkstra para obter um caminho de menor custo acumulado.

---

## Objetivos

- extrair um grafo real de ruas a partir do OpenStreetMap;
- representar esse grafo com listas de adjacência;
- implementar manualmente BFS e Dijkstra;
- analisar conectividade e estatísticas do grafo;
- comparar distância estrutural versus custo funcional;
- visualizar os caminhos encontrados.

---

## Modelagem do Grafo

O grafo é construído a partir de vias do tipo drive obtidas com OSMnx. Cada cruzamento vira um vértice e cada conexão viária vira uma aresta direcionada na estrutura interna usada pelo programa.

Depois da extração, cada aresta recebe um peso aleatório para simular o custo de travessia em diferentes biomas:

| Bioma | Peso | Faixa/Regra | Probabilidade |
|------|------|-------------|---------------|
| Terra | 2 | valor fixo | 50% |
| Água | 10 | valor fixo | 25% |
| Deserto | 20 a 25 | sorteado | 15% |
| Fogo | 50 a 100 | sorteado | 10% |

---

## Algoritmos Implementados

### BFS

Usado para encontrar um caminho entre origem e destino com menor número de passos na estrutura do grafo.

- Complexidade: O(V + E)
- Estruturas: fila e conjunto de visitados

### Dijkstra

Usado para encontrar o caminho de menor custo acumulado considerando os pesos dos biomas.

- Complexidade da implementação atual: O(V²)
- Estruturas: dicionários de distância e predecessor, além do conjunto de não visitados

---

## Análises Realizadas

O programa calcula:

- número de vértices e arestas;
- grau médio, máximo e mínimo;
- vértice de maior conectividade;
- detecção simples de presença de ciclos;
- existência de caminho entre origem e destino;
- custo total do caminho retornado por BFS e Dijkstra;
- economia percentual obtida pelo Dijkstra.

---

## Visualização

O script gera uma figura com dois painéis:

- painel esquerdo: caminho encontrado por BFS;
- painel direito: caminho encontrado por Dijkstra;
- marcador verde: origem;
- marcador vermelho: destino.

As arestas são coloridas conforme o peso associado ao bioma.

O arquivo gerado é analise_grafos_unifor.png.

---

## Como Executar

### Dependências

```bash
pip install osmnx networkx matplotlib
```

### Execução

```bash
python AV3/trabFinal.py
```

### Saídas

- terminal com estatísticas e comparação dos caminhos;
- imagem analise_grafos_unifor.png com a visualização.

---

## Coordenadas Atuais

- Residência: (-3.7590, -38.5837)
- UNIFOR: (-3.7733, -38.4760)

Esses valores podem ser alterados diretamente na função main.

---

## Cache e Internet

O projeto usa cache local do OSMnx para evitar downloads repetidos do mesmo mapa. A pasta de cache foi fixada em AV3/cache, evitando duplicação quando o script é executado a partir de diretórios diferentes.

Na primeira execução sem cache, é necessária conexão com a internet.

Se o download falhar, o programa informa o erro e encerra. A versão atual não possui fallback automático para um grafo sintético.

---

## Estrutura Atual do Código

O arquivo trabFinal.py está organizado em funções para:

- bfs;
- dijkstra;
- reconstrução do caminho mínimo;
- cálculo de estatísticas;
- teste de conectividade;
- extração dos dados do OpenStreetMap;
- impressão dos resultados;
- visualização gráfica;
- configuração do cache do OSMnx;
- execução principal em main.

---

