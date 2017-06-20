"""
A more proper DFS algorithm is probably required for the purpose of properly getting this in shape.
Another possible solution for this problem is the following:
The directed graph will be such that there will be a start node and from there we will be able to travel to all nodes in the first row except the node 0,0. From the second node in the first row, 0,1 we will be able to travel to all nodes in the first row except 1,1. From the nodes third node in the first row, 0,2 we will be able to travel to all nodes in the second row except 2,2. And so on for all nodes in the entire graph.
Now the idea is that we can start with a dictionary of all nodes, the keys are tuples describing the node positions and the values are the number of bunnies collected at any instance and the time taken also stored in the form of a tuple.

"""