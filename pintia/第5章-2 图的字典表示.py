def f():
    n=eval(input())
    graph={}
    for i in range(n):
        node=eval(input())
        for j in node:
            graph[j]=node[j]
    nodes=0
    edges=0
    total_length=0
    for item in graph:
        nodes+=1
        for edge in graph[item]:
            edges+=1
            total_length+=graph[item][edge]
    return nodes,edges,total_length
if __name__=="__main__":
    nodes, edges, total_length=f()
    print(nodes,edges,total_length)