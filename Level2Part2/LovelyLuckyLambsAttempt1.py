# import math
def answer(total_lambs):
    # stringent case
    maxNumber=0
    minNumber=0
    if total_lambs>=10 and total_lambs<=10**9:
        a=1
        b=1
        maxNumber=2
        S=2
        while True:
            t=a+b
            S=t+S
            if S>total_lambs:
                break
            else:
                maxNumber+=1
                a=b
                b=t
        # print('minNumber:'+str(maxNumber))
        # above we will get stringent case 
        minNumber=0
        S=0
        t=1
        while True:
            S=t+S
            if S>total_lambs:
                break
            else:
                minNumber+=1
                t=2*t
    # print('maxNumber:'+str(minNumber))
    # minNumber=int(math.log(total_lambs+1,2))
    return maxNumber-minNumber

print('enter total_lambs')
t=int(input())
print(answer(t))



