"""
This is a test program designed to test whether in recursion, list instances are saved at each level of the recursion and during back tracking, whether we actually list instances that are saved are available.

Result: States for lists are not saved

"""
import random
import sys
def test(a, depth):
    if depth==5:
        # sys.exit()
        exit()
        return
    else:
        depth+=1
        a.append(random.randrange(1, 10))
        test(a, depth)
        print('backtracking information: a: {} at depth: {}'.format(a, depth))
        a.pop(0)

test([], 0)