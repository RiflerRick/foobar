"""
Clearly the naive approach is not going to work in all possible cases. One point of failure for the above approach was that each time trying to find the least time and going for that may not be accurate. 

For instance if we are at the bulkhead and it is found that the least distance is at start, we go to start instead of trying to save a bunny. This may lead to less number of bunnies rescued.
On the other hand for some other case it may be necessary to actually go to start from where we can gain time and actually save more bunnies than trying to save a bunny first hand.

Clearly the accurate approach would be a graph algorithm.
"""
bunniesSaved=[]
def traverse(depth, row, times, time_limit, bunnies):
    """
    One definite approach can be a DFS algorithm. 
    We first try to get all the bunnies, then if the time is negative after getting all bunnies, we keep backtracking eliminating bunnies one by one until the time is positive at which point we can simply return. Another important idea is that we need to consider that during backtracking the first time the time_limit is not negative and the guy is at the bulkhead, thats the time we actually see how many bunnies we could save, we can return after that.
    the variable depth is just for debugging purposes
    """
    # depth keeps track of the real depth reached. During backtracking of the depth goes to zero, it 
    # means that we have come back up to the start in the route.
    # row denotes the row where i am (i in the question is the one trying to save a bunny)
    # bunnies is the list where bunnies are appended
    # print('row: {}'.format(row))
    if len(bunnies)==len(times)-2:
        # stopProcess(bunnies)
        print('depth : {}'.format(depth))
        return

    for a in range(len(times)):

        if a != row:
            
            if a != 0 and a != len(times)-1:
                if a-1 in bunnies:
                    continue
                else:
                    bunnies.append(a-1)
            depth+=1
            time_limit-=times[row][a]
            print('row now: {}'.format(row))
            traverse(depth, a, times, time_limit, bunnies)
            # backtracking code comes here
            if depth==1:
                # it means we have reached the very first level again.
                print('reached level 1')
                time_limit=realTimeLimit
                depth=0
                continue

            if time_limit<0:
                print('time_limit now: {}, depth now: {} and bunnies: {}'.format(time_limit, depth, bunnies))
                if bunnies!=[]:
                    bunnies.pop(0)
                

            else:
                if row==len(times)-1:
                    if len(bunnies)>len(bunniesSaved):
                        bunniesSaved=bunnies[:]
                continue
            
def stopProcess(bunnies):
    print(bunnies)
    exit()

start=0
times=[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
realTimeLimit=1
time_limit=realTimeLimit
traverse(0, start, times, time_limit, [])

print(bunniesSaved)

                

