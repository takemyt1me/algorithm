N, M, K = map(int, input().split())
#N 노드 개수, M 간선 개수, K 시작 노드
graph1 = {node: [] for node in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph1[a].append(b)
    graph1[b].append(a)

visit_dfs = list()
visit_bfs = list()

def DFS(graph, start_node):
    visit_dfs.append(start_node)
    for each_node in sorted(graph[start_node]):
        if (each_node in visit_dfs) == False:
            DFS(graph, each_node)

def BFS(graph, start_node):
    visit_bfs.append(start_node)
    queue = list()
    queue.append(start_node)
    while len(queue) >0:
        for each_node in sorted(graph[queue[0]]):
            if (each_node in visit_bfs) == False:
                visit_bfs.append(each_node)
                queue.append(each_node)
        del queue[0]

DFS(graph1, K)
BFS(graph1, K)

for node in visit_dfs:
    print(node, end=' ')
print()
for node in visit_bfs:
    print(node, end =' ')