graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=set()
visited2= []
queue = []

def bfs(visited2, graph, node):
  visited2.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited2:
        visited2.append(neighbour)
        queue.append(neighbour)


def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
    for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

while(True):
    print("Select one option to Traversal of the graph!")
    print("\n 1.DFS \n 2.BFS")
    a = int(input("Enter your choice:"))
    if a == 1:
        print("The DFS of given graph is give below")
        dfs(visited, graph, node='5')
    elif a == 2:
        print("The BFS of given graph is given below:")
        bfs(visited2, graph, node='5')
    else:
        break



