"""
The problem is no wonder interesting. A possible naive approach to solve the problem would simply be to start from the very first row, find out the least number in that row, find out its position and go to that number row each time. Simultaneously we need to keep track of time. A solution using this naive approach would be the following.
"""
def answer(times, time_limit):
    # your code here
    rows=len(times)
    cols=rows
    time=time_limit
    i=0
    bunnies=[]
    pos=0
    while True:
        if time<0 and pos!=cols-1 and pos!=0:
            print('first block', end='')
            
            # it means we need to try and add time, if we want to save any more bunnies.
            if i != 0:
                # we cannot take the minimum value as the value of the row
                minVal=times[i][0]
                pos=0
            else:
                minVal=times[i][1]
                pos=1

            for j in range(cols):
                if times[i][j]< minVal and j!=i and j-1 not in bunnies:
                    minVal=times[i][j]
                    pos=j
                    
            time-=times[i][pos]
            if time>=0:
                # we can continue
                if pos!= 0 and pos!= cols-1:
                    bunnies.append(pos-1)
                    # i=pos
            else:
                bunnies.pop()
                break

        elif time<0 and pos==0:
            print('second block', end='')
            if i != 0:
                    # we cannot take the minimum value as the value of the row
                minVal=times[i][0]
                pos=0
            else:
                minVal=times[i][1]
                pos=1

            for j in range(cols):
                if times[i][j]< minVal and j!=i and j-1 not in bunnies:
                    minVal=times[i][j]
                    pos=j
                    
            time-=times[i][pos]
            if time>=0:
                # we can continue
                if pos!= 0 and pos!= cols-1:
                    bunnies.append(pos-1)
                    # i=pos
            else:
                break

        else:
            print('third block', end='')
            if i != 0:
                # we cannot take the minimum value as the value of the row
                minVal=times[i][0]
                pos=0
            else:
                minVal=times[i][1]
                pos=1

            for j in range(cols):
                if times[i][j]< minVal and j!=i and j-1 not in bunnies:
                    minVal=times[i][j]
                    pos=j

            # print ('i, pos : {}, {} and minVal: {} '.format(i, pos, minVal), end='')
            time-=times[i][pos]
            # print(' time: {}'.format(time))
            # i=pos
            if pos!= 0 and pos!= cols-1:
                bunnies.append(pos-1)

        print ('  i, pos : {}, {} and minVal: {} '.format(i, pos, minVal), end='')
        print(' time: {}'.format(time), end='')
        print('  bunnies: {}'.format(bunnies))
        i=pos

    bunnies.sort()
    print(bunnies)

# times=[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
times=[[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
time_limit=3
answer(times, time_limit)
