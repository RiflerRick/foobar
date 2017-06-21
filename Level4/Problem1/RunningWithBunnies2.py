"""
A more proper DFS algorithm is probably required for the purpose of properly getting this in shape.
Another possible solution for this problem is the following:
The directed graph will be such that there will be a start node and from there we will be able to travel to all nodes in the first row except the node 0,0. From the second node in the first row, 0,1 we will be able to travel to all nodes in the first row except 1,1. From the nodes third node in the first row, 0,2 we will be able to travel to all nodes in the second row except 2,2. 

"""
def answer(time_limit, times):
    states={}
    start='startNode'
    nodes=[]
    nodes.append(start)
    while nodes !=[]:
        currentNode=nodes.pop()
        if currentNode==start:
            time=time_limit
        else:
            time=states[currentNode][1]
        # prevBunnies=states[currentNode][0][:]
        # now we get the neighbors of currentNode and push them onto the stack
        if currentNode==start:
            # then we go over the nodes in the same row except ofcourse the first node
            for i in range(1, len(times)):
                bunnies=[]
                position=(0, i)
                timeNow=times[position[0]][position[1]]
                if i in range(1, len(times)-1):# if the i value is in the range of bunnies, include them
                    bunnies.append(i)
                nodes.append(position)
                states[position]=(bunnies, time-timeNow)
                                                    
                    
        else:
            for i in range(len(times)):
                bunnies=states[currentNode][0][:]
                if i !=currentNode[1] and i not in bunnies:
                    
                    position=(currentNode[1], i)
                    timeNow=times[position[0]][position[1]]
                    if i in range(1, len(times)-1):
                        bunnies.append(i)
                    if position not in states:
                        nodes.append(position)
                        states[position]=(bunnies, time-timeNow)
                    else:
                        if len(bunnies)>=len(states[position][0]):
                            print('current bunnies more than previous bunnies')
                            if (time-timeNow)>=states[position][1]:
                                states[position]=(bunnies, time-timeNow)
                                nodes.append(position)

    for i in states:
        print('{}:{}'.format(i, states[i]))

times=[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
time_limit=1     
answer(time_limit, times)
        
