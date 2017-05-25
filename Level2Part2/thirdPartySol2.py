def answer(total_lambs):
    doubleList=[]
    x=0
    runningTotal=0
    while x<=total_lambs:
        currentValue=2**x
        doubleList.append(currentValue)
        runningTotal=runningTotal+currentValue
        if runningTotal>total_lambs:
            break
        x=x+1
    
    fibList=[1,1]
    fibRunningTotal=2
    y=2
    while y<=total_lambs:
        value=fibList[y-1]+fibList[y-2]
        fibList.append(value)
        fibRunningTotal=fibRunningTotal+int(fibList[y])
        if fibRunningTotal>total_lambs:

            break

        y=y+1
    
    return len(fibList)-len(doubleList)

print(answer(10))