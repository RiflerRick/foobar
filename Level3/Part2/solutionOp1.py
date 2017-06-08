"""
This is another of those problems where there is some math involved and all you need to do is to simply recognize what type of math is involved in finding the answer. Its pretty basic actually. Here the math involved is co-primes. Basically what we are given are 2 numbers and all we need to do is to find out whether they are co prime or not. If 2 numbers are co prime, then they do not have any other factors common between them except 1. 
Here we start from the 2 numbers given to us. M and F
A naive approach of solving this problem would be to subtract the bigger number from the smaller one at each step of the problem to arrive at 1, 1. If we are able to arrive at 1,1 it means that the 2 numbers are co-prime. If not they are not co-prime. At each step of the subtraction we increment a counter and hence arrive at the right solution in the end. This approach however will give a TLE.
A better approach as is clear is using the Euclidean algorithm. Here instead of subtraction we use the modulo operator at each step. The while loop in the solution does exactly that. The counter in this case is not incremented by one. Instead it is incremented by p/q where p and q are the 2 numbers being solved for modulus i.e. p modulo q. Whats important here is that by doing p/q we are actually traversing traversing all those steps of the subtraction method in one go. Thats is where the optimization is happening.
Its a cool problem. Easy though.
"""
def answer(M, F):
    a=int(M)
    b=int(F)
    c=0
    if a>b:
        p=a
        q=b
    else:
        p=b
        q=a
    while q!=0:
        t=q
        q=p % t
        c+=int(p/t)
        p=t
    if p==1:
        c-=1
        return c
    else:
        return 'impossible'

# print(answer('2','4'))
        