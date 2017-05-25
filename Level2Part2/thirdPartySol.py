import math
def answer_lamb_worked(total_lambs):
    
    phi = (1+math.sqrt(5))/2  # golden search ratio
    tau = (1-math.sqrt(5))/2  # equal to 1/phi
    eps = math.pow(10, -10)

    max_hunchmen = int(round(math.log((total_lambs + 1) * math.sqrt(5)+eps, phi))) - 2
    Fib_num = int(round((math.pow(phi, max_hunchmen+2)-math.pow(tau, max_hunchmen+2))/math.sqrt(5)))
    if total_lambs+1 < Fib_num:
        max_hunchmen -= 1

    min_hunchmen = int(math.log((total_lambs + 1), 2))

    return max_hunchmen - min_hunchmen

print('enter total_lambs')
total_lambs=int(input())
print(answer_lamb_worked(total_lambs))