import math

print('enter n:')
n=int(input())
a=(1+math.sqrt(5))/2
print('nth term:'+str(round((1/math.sqrt(5)* math.pow(a,n+1) ))  ) )