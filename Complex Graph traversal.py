import threading
from collections import defaultdict

def run_node(node_id, name, graph, indegree, visited, lock, node_map):
    with lock:
        if node_id in visited:
            return
        print("Executing node:", name)
        visited.add(node_id)

    children = graph[node_id]
    for child in children:
        with lock:
            indegree[child] -= 1
            if indegree[child] == 0:
                th = threading.Thread(target=run_node,
                                      args=(child, node_map[child], graph, indegree, visited, lock, node_map))
                th.start()
                threads.append(th)
            else:
                print(f"Waiting for other parents of {node_map[child]}")

n = int(input("Enter number of nodes: "))
node_map = {}
for _ in range(n):
    raw = input()
    if ":" not in raw:
        continue  # skip bad input
    key, val = raw.split(":")
    node_map[int(key.strip())] = val.strip()

m = int(input("Enter number of edges: "))
graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(m):
    edge = input()
    if ":" not in edge:
        continue
    src, dest = edge.split(":")
    src = int(src.strip())
    dest = int(dest.strip())
    graph[src].append(dest)
    indegree[dest] += 1

for node in node_map:
    if node not in indegree:
        indegree[node] = 0

visited = set()
lock = threading.Lock()
threads = []

start_node = 1
print("Starting workflow from root:", node_map[start_node])
t = threading.Thread(target=run_node,
                     args=(start_node, node_map[start_node], graph, indegree, visited, lock, node_map))
t.start()
threads.append(t)

for t in threads:
    t.join()

print("Total nodes executed:", len(visited))
