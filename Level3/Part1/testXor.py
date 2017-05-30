a=7844
ans=0
while a<7900:
    ans=ans^a
    a+=1
    if a%2==0:
        print(ans)

# in case the first number is an even number
# alternating 1, 0 starting from 1--> pattern is the following: 1, nextNum, 0, sameNum, 1