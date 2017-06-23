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
import functools
permutations=[]

def comp(a, b):
    # a, b are 2 lists in a list of lists
    if len(a)!=len(b):
        return len(b)-len(a)
    else:# lengths are equal
        return sum(a)-sum(b)

def getSelections(numberOfBunnies):
    numSelections = 2**(numberOfBunnies)-1
    maxLength=len("{0:b}".format(numSelections))
    numbers=[]
    for i in range(1, numSelections+1):
        a=list("{0:b}".format(i))
        if len(a) != maxLength:
            for i in range(len(a), maxLength):
                a=['0']+a
        numbers.append(a)
    # now we have got all the numbers
    # print('numbers: {}'.format(numbers))
    selections=[]
    s=[]
    for i in numbers:
        s=[]
        for j in range(len(i)):
            if i[j]=='1':
                s.append(j)
        
        selections.append(s)
    # print('selections now: {}'.format(selections))
    # [[0, 1, 2], [0, 1], [0, 2], [1, 2], [0], [1], [2], []]
    selections=sorted(selections, key=functools.cmp_to_key((comp)))
    # selections.reverse()
        

    # for i in range(len(selections)): # simple selection sort here because we dp not need to fancy sorting simply because the max number possible is 2**5-1=31
    #     maxVal=len(selections[i])
    #     pos=i
    #     for j in range(i+1, len(selections)):
    #         if len(selections[j])>maxVal:
    #             maxVal=len(selections[j])
    #             pos=j

    #     temp=selections[i][:]
    #     selections[i]=selections[pos][:]
    #     selections[pos]=temp[:]
    
    # print(selections)
    return selections
    
def permute(a, l, r):
    if l==r:
        # print (str(a))
        permutations.append(a[:])
        # yield a
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack        

def answer(times, time_limit):
    MAXVALUE=10000000
    minMatrix=[]
    #initialization of matrix
    for x in range(len(times)):
        minMatrix.append([])
        for y in range(len(times)):
            minMatrix[x].append(0)


    # print(minMatrix)

    for i in range(len(times)):
        for src in range(len(times)):
            if i==0:
                for p in range(len(times)):
                    minMatrix[src][p] =  MAXVALUE
                minMatrix[src][src]=0
            
            for a in range(len(times)):
                for b in range(len(times)):
                    if minMatrix[src][a]!=MAXVALUE and minMatrix[src][a] + times[a][b] < minMatrix[src][b]:
                        minMatrix[src][b] = minMatrix[src][a] + times[a][b]

    # print('minMatrix: {}'.format(minMatrix))
    # 0,2,1,1,-1,
    # 8,0,1,1,-1,
    # 8,2,0,1,-1,
    # 8,2,1,0,-1,
    # 9,3,2,2,0,

    for src in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                if minMatrix[src][i] + times[i][j] < minMatrix[src][j]:
                    result=[]
                    for p in range(len(times)-2):
                        result.append(p)
                    return result

    selections=getSelections(len(times)-2)
    # print('permutations')

    for i in range(len(selections)):
        permute(selections[i][:], 0, len(selections[i])-1)
        # print(permutations)
        

        for perm in permutations:
            fromPosition = 0
            time = time_limit
            # print('perm now: {}'.format(perm))
            for val in perm:
                time -= minMatrix[fromPosition][val + 1]
                fromPosition = val + 1

            time -= minMatrix[fromPosition][len(times)-1]
            if time>=0:
                print('selection now: {}'.format(selections[i]))
                del permutations[:]
                return selections[i]

            

        del permutations[:]

    return [] # if nothing can be saved
        # print('---------------------')

        
            
        
        # for j in range(len(permutations)):
        #     f=0
        #     time=time_limit



    
# getSelections(3)
answer( [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)

answer( [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)

    

                
        
