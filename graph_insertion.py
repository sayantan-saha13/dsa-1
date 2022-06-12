def insert(n):
    global node_count
    if n in node:
        print("node is present")
    else:
        node_count= node_count +1
        node.append(n)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def add_edge(e1,e2):
    if e1 not in node:
        print("not present")
    elif e2 not in node:
        print("not present")
    else:
        index_1=node.index(e1)
        index_2=node.index(e2)
        graph[index_1][index_2]=1
        graph[index_2][index_1]=1
def delete_node(n):
    global node_count
    if n not in node:
        print("not present")
    else:
        index1=node.index(n)
        node_count=node_count-1
        node.remove(n)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
def delete_edge(e1,e2):
    if e1 not in node:
        print("not present")
    elif e2 not in node:
        print("not present")
    else:
        index1=node.index(e1)
        index2=node.index(e2)
        graph[index1][index2]=0
        graph[index2][index1]=0
def show_matrix():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


node = []
graph = []
node_count = 0
print("Before adding Nodes")
print(node)
print(graph)
insert("A")
insert("B")
insert("D")
print("after adding node and edges")
add_edge("A","B")
add_edge("A","D")
print(node)
print(graph)
print("after deleting the nodes: ")
delete_node("D")
print("after deleting edge")
delete_edge("A","D")
print("The matrix is: \n")
show_matrix()
print()
print(node)
print(graph)