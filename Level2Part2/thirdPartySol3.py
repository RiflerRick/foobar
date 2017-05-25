import math

def answer(total_lambs):
    phi = (1+math.sqrt(5))/2  
    tau = (1-math.sqrt(5))/2  
    # eps = math.pow(10, -10)
    
    max_hunchmen = int(round(math.log((total_lambs + 1) * math.sqrt(5), phi))) - 2
    print('maxHunchmen: '+str(max_hunchmen))
    Fib_num = int(round((math.pow(phi, max_hunchmen+2)-math.pow(tau,max_hunchmen+2))/math.sqrt(5)))
    print('fibNum: '+str(Fib_num))
    if total_lambs+1 < Fib_num:
      max_hunchmen -= 1
      print('maxHunchmen: '+str(max_hunchmen))
    elif total_lambs + 1 == Fib_num:
        total_lambs = Fib_num
    if (total_lambs + 1) % 2 == 0:
         min_hunchmen = int(round(math.log((total_lambs + 1), 2)))
    else:
        min_hunchmen = int(math.log((total_lambs + 1), 2))
    
    return abs(max_hunchmen - min_hunchmen)

total_lambs=int(input())
print(answer(total_lambs))