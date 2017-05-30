def answer(start, length):
    
    numbersToTraverse=length*length

    end=start+(numbersToTraverse)

    val=end-length # number to start xoring from, in this case the end

    checksum=start

    skip=length-2

    num=val

    counterSkip=1

    counter=length-counterSkip

    debugCounter=0

    while num>start:
        
        debugCounter+=1

        if counter%length==0 and counter!=0:
            num-=skip
            skip-=1
            counterSkip+=1
            counter=length-counterSkip
            
        else:
            checksum=checksum^num
            num-=1
            counter+=1
        
    print('debugCounter:'+str(debugCounter))
    return checksum

print(answer(4,4))
            
            
        

