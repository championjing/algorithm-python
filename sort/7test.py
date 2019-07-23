# coding=UTF-8
def find_shortest_node(costs,process):
    shortest_value = float('inf')
    shortest_node = None
    for key in costs :
        if costs[key] < shortest_value and key not in process:
            print( 'key:'+key +'->'+ str(costs[key]) )
            shortest_node = key
            shortest_value = costs[key]
    return shortest_node
# 图-》主要的数据库存储
graph = {}
graph['a'] = {}
graph['a']['b'] = 5
graph['a']['c'] = 2

graph['b'] = {}
graph['b']['d'] = 4
graph['b']['e'] = 2

graph['c'] = {}
graph['c']['b'] = 8
graph['c']['e'] = 7

graph['d'] = {}
graph['d']['f'] = 3
graph['d']['e'] = 6

graph['e'] = {}
graph['e']['f'] = 1

graph['f'] = {}
# 起点到各点的最小距离
costs = {}
# 标记已经处理过的值
process = []
# 记录最小路径的经过
parents = {}
infinity = float('inf')
# init costs
start = 'a'
end = 'f'
for node in graph.keys():
    if node == start:
        costs[node] = 0
    else:
        costs[node] = infinity

print( str(costs) )
# 调用方法，找到未处理过的路径最短的点
node = find_shortest_node(costs,process)
while len( graph.keys() ) > 0:
    print( "shortest temp :" + node)
    neighbours = graph[node]
    for one_neithbour in neighbours.keys():
        old_length = costs[one_neithbour]
        # 当前节点到邻居的距离加上当前节点
        new_length = graph[node][one_neithbour] + costs[node]
        if new_length < old_length:
            costs[one_neithbour] = new_length
            parents[one_neithbour] = node
    del graph[node]
    process.append(node)
    node = find_shortest_node(costs,process)

print( str(costs) )
print( str(parents) )
