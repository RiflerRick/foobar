"""
For this final solution we are going to follow a third party solution available online. First we are going to find all possible selections of the number of bunnies possible. For instance if we have a total of 3 bunnies-> [0,1,2] then we first find out all possible combinations of the selection of these bunnies. This includes, [1,2,3],[1],[2],[3],[1,2],[2,3],[1,3]. 

Subset preparation(basically selection of bunnies in all possible ways):
The selection is done in a rather clever way. Firstly observe that the number of ways of all possible selection of bunnies = nCn + nC(n-1) + nC(n-2) + ... + nC1 = 2**n - 1, where n is the total number of bunnies. One important idea here is that the possible selections can be found out using the binary set of numbers from 1 to 2**n - 1. Now if we observe the positions of 1 in all these numbers then we can actually find the all possible selections of these numbers. Its an interesting, consequence of the fact that we have 2**n-1 numbers in total.

Now a bit of graph theory:
What follows is an algorithm similar to the Floyd–Warshall algorithm. What we are doing here is the following.
min=[[]]
for i in range(len):
    for src in range(len):
        if i==0:
            for p in range(len):
                min[src][p] = MAXVALUE # MAXVALUE is a maximum value possible 
            min[src][src]=0
        
        for a in range(len):
            for b in range(len):
                if min[src][a]!=MAXVALUE and min[src][a] + times[a][b] < min[src][b]:
                    min[src][b] = min[src][a] + times[a][b]

The above block of code basically makes sure that from a certain position in the graph if we are travelling to another position in the same row, then it must be having the least time.

Next we find out all possible permutations of the selections that e just did. Then we apply the permutations and find out in which case we get the best results.

"""