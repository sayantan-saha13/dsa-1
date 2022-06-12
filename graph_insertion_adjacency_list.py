def add_node(a):
    if a in graph:
       print(a,"already presnet")
    else:
        graph[a]=[]
def add_edge(e1,e2):
    if e1 not in graph:
        print("not present in graph")
    elif e2 not in graph:
        print("not present")
    else:
        graph[e1].append(e2)
        graph[e2].append(e1)
def delete_node(n):
    if n not in graph:
        print("not present")
    else:
        graph.pop(n)
        for i in graph:
            list=graph[i]
            if n in list:
                list.remove(n)
def delete_edge(e1,e2):
    if e1 not in graph:
        print("not present in graph")
    elif e2 not in graph:
        print("not present")
    else:
        if e2 in graph[e1]:
          graph[e1].remove(e2)
          graph[e2].remove(e1)
def Dfs(node,visisted,graph):
    if node not in graph:
        print("not present")
        return
    if node not in visited:
        print(node)
        visisted.add(node)
        for i in graph[node]:
            Dfs(i,visisted,graph)
def Dfs_iterrative(node,graph):
    visited=set()
    if node not in graph:
        print("not present")
        return
    stack=[]
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


visited=set()
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)
print()
delete_edge("B","C")
#delete_node("A")
print(graph)
#Dfs("A",visited,graph)
Dfs_iterrative("A",graph)