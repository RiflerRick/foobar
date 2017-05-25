import math
def parent(height, node):
    size=int(math.pow(2,height))-1
    if node==size:
        return -1
    before=0

    while True:
        size=int(size/2)
        left=before+size
        right=left+size
        me=right+1
        if left==node or right==node:
            return me
        if node>left:
            before=left

def answer(h,q):
    ans=[]
    for i in q:
        ans.append(parent(h, i))
    print(ans)

def main():
    answer(5, [19, 14, 28])

if __name__=="__main__":
    main()