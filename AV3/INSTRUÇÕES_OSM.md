# Instruções para Usar Dados Reais do OpenStreetMap

## Visão Geral

O projeto usa dados reais do OpenStreetMap por meio da biblioteca OSMnx para montar um grafo viário de Fortaleza e comparar os caminhos obtidos por BFS e Dijkstra.

O fluxo atual do programa é direto:

- baixa ou reaproveita do cache a malha viária da região entre a residência e a UNIFOR;
- converte o grafo retornado pelo OSMnx para listas de adjacência próprias;
- aplica pesos aleatórios nas arestas para simular biomas de risco;
- executa BFS e Dijkstra;
- gera uma visualização comparativa em imagem.

## Como Executar

No terminal, a partir da pasta do projeto:

```bash
python AV3/trabFinal.py
```

O script não exibe menu de escolha de fonte de dados. Ele executa diretamente a extração via OpenStreetMap.

## Coordenadas Utilizadas

As coordenadas configuradas atualmente no código são:

- Residência: (-3.7590, -38.5837)
- UNIFOR: (-3.7733, -38.4760)

Se quiser alterar a origem, edite a função main em trabFinal.py e substitua a tupla de residencia pelas coordenadas desejadas.

## Raio de Extração

A função extrair_dados_osm usa por padrão um raio de 4000 metros.

Trecho atual:

```python
dados = extrair_dados_osm(residencia, unifor)
```

Se quiser ajustar a área analisada, altere a assinatura da função ou passe o parâmetro distancia_raio explicitamente na chamada.

Sugestões:

- 2000: área menor e download mais rápido;
- 4000: valor atual do projeto;
- 5000 ou mais: área maior, com mais vértices e mais tempo de processamento.

## Dependências

Instale as bibliotecas necessárias com:

```bash
pip install osmnx networkx matplotlib
```

## Cache Local

O cache do OSMnx foi centralizado em AV3/cache.

Isso significa que:

- execuções futuras tendem a ser mais rápidas;
- a pasta cache na raiz do workspace não é mais necessária para o script atual;
- se você quiser limpar o cache, pode apagar o conteúdo de AV3/cache e o mapa será baixado novamente na próxima execução.

## Saídas Geradas

Ao rodar o programa, você terá:

- saída textual no terminal com estatísticas do grafo e comparação entre BFS e Dijkstra;
- arquivo analise_grafos_unifor.png com a visualização dos dois caminhos.

## Observações Importantes

### Internet

Na primeira execução sem cache, é necessário acesso à internet para baixar os dados do OpenStreetMap.

### Falha no Download

Se o download falhar, o programa atualmente apenas informa o erro e encerra. Não existe fallback automático para grafo sintético na versão atual do código.

## Resumo Técnico

- Fonte de dados: OpenStreetMap via OSMnx;
- Tipo de rede: drive;
- Representação interna: listas de adjacência;
- Pesos dos biomas: 2, 10, 20-25 e 50-100;
- Algoritmos implementados: BFS e Dijkstra.
