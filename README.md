# ApiWiz

# APIwiz Assignment – Workflow Graph Execution

## What this does

This script takes a set of nodes and edges representing a workflow (like a directed graph), and then runs each node in the right order. A node only runs once all of its parent nodes have finished. If a node has multiple children, those can run in parallel.

The goal is to print the node names in the order they are executed, and also print how many nodes got executed in total.

---

## How I approached it

1. I read the number of nodes and built a map that links node IDs to their names.
2. Then I read the edges and built a graph using a dictionary of lists.
3. I also kept track of how many incoming edges (parents) each node has.
4. I used Python’s `threading` library to run child nodes in parallel where possible.
5. Each node only runs when its `indegree` is 0, meaning all its parents are done.
6. After starting all the threads, I waited for them to finish.

---

## Tools and Libraries Used

- Python 3
- `threading` – to simulate parallel execution
- `collections.defaultdict` – for graph and indegree map
- Just built-in libraries, nothing external

---

## Assumptions

- Node 1 is always the starting point.
- The graph is valid and has no cycles.
- Input is entered correctly as per the given format.
- Output order might change slightly because of threading, but rules are respected.

---

## Example Output

Starting workflow from root: Node-1
Executing node: Node-1
Executing node: Node-2
Executing node: Node-3
Executing node: Node-4
Executing node: Node-5
Total nodes executed: 5


---

## Final Notes

I added a few extra `print()` lines for debugging or clarity, just to make sure I could follow the flow while testing. The structure is simple and straightforward, and I didn’t use any frameworks or outside help.

