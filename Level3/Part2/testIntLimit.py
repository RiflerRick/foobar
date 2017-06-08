a='1'
for i in range(50):
    a+='0'

b=int(a)
c=0
b-=25
print(b)
while b>0:
    c+=1
    b=int(b/10)



print(b)
print(c)