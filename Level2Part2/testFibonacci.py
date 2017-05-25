import math

# print('enter n:')
# n=int(input())
# a=(1+math.sqrt(5))/2
# print('nth term:'+str(round((1/math.sqrt(5)* math.pow(a,n+1) ))  ) )

def answer(total_lambs):

    maxNumber=0
    phi=(1+math.sqrt(5))/2
    arg1=((math.sqrt(5)*(total_lambs+1))/(1+phi))-1
    maxNumber=round(math.log(arg1,phi))

    minNumber=round(math.log(total_lambs+1,2))

    return maxNumber-minNumber

print('enter total_lambs')
total_lambs=int(input())
print('answer:'+str(answer(total_lambs)))
