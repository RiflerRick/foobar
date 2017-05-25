import math
count=1
class hello:
    def __init__(self):
        self.dummy=2
q=[]


def buildSkippingSequence(numLowerTrees):
    l=[0 for i in range(int(numLowerTrees)-1)]
    midValue=int(math.log(numLowerTrees, 2))
    populateSequence(0, len(l)-1, l, midValue)
    print (l)

def populateSequence(start, end, l, midValue):
    print("midValue now:"+str(midValue))
    if midValue==0:
        return
    print("start: "+str(start))
    print("end: "+str(end))
    mid=int((end+start)/2)
    l[mid]=midValue
    populateSequence(start, mid, l, midValue-1)
    populateSequence(mid+1, end, l, midValue-1)
    # print("l now:"+str(l))


def main():
    a=[]
    for i in range(int(math.pow(2,15))):
        a.append(i)
    buildSkippingSequence(32)

def check(query):
    query.remove(2)

if __name__=="__main__":
    main()