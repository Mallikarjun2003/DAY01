visited =set()
source = 5
destination = 2
res =[]
g = {
    5:[(7,2),(3,1)],
    7:[(5,2),(4,9),(3,4)],
    4:[(7,9),(8,1),(2,4)],
    8:[(3,6),(4,1),(2,4)],
    3:[(5,1),(7,4),(8,6)],
    2:[(4,4),(8,4)]
}
res =[]

def dfs(node,path,visited,cost):
    global res
    if node and node not in visited:
        path.append(node)
        visited.add(node)
        if node == destination:
            # print(path)
            
            if not res or res[1] > cost:
                res = (path[:],cost)
        else:
            for n,ecost in g[node]:
                # print(g[n])
                dfs(n,path,visited,cost +ecost)
        visited.remove(node)
        path.pop()
dfs(source,[],visited,0)

print(res)
