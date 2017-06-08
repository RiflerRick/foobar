def answer(M, F):
    a=int(M)
    b=int(F)
    c=0
    while True:
        if a==1 and b==1:
            return c
        elif a<1 or b<1:
            return 'impossible'
        if a>b:
            a=a-b
            c+=1
            continue
        else:
            b=b-a
            c+=1
            continue
# print(answer('2','4'))