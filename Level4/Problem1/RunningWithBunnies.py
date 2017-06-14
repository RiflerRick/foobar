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
    while True:
        if i != rows-1:
            minVal=times[i][i+1]
        else:
            minVal=times[i][i-1]
        for j in range(cols):
            if times[i][j]< minVal and j!=i:
                minVal=times[i][j]
                pos=j
        time-=times[i][pos]
        i=pos
        if pos!= 0 or pos!= cols-1:
            bunnies.append(pos)
        if time < 0 and pos != cols-1: # that is time is already negative and we have not reached the bulkhead it means that if we don't gain time some how there is no time left
            if i != rows-1:
                minVal=times[i][i+1]
            else:
                minVal=times[i][i-1]
            for j in range(cols):
                if times[i][j]<minVal and j!=i:
                    minVal=times[i][j]
                    pos=j
            time-=times[i][pos]
            if time>=0:
                # we can continue
                if pos!=cols-1:
                    bunnies.append(pos)
            else:
                bunnies.pop(0)
                break
                
    bunnies.sort()
    print(bunnies)

times=[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
time_limit=1
answer(times, time_limit)
