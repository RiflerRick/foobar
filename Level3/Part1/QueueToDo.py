def answer(start, length):
    
    numbersToTraverse=length*length

    end=start+(numbersToTraverse)

    val=end-length # number to start xoring from, in this case the end

    checksum=start

    skip=length-2

    counter=length-1

    num=val

    while val>=start:
        # print('counter: ' +str(counter))
        # print('val: '+str(val))
        if counter%length==0:
            num-=skip
            skip-=1
        else:
            # print('num: '+str(num))
            # print('val: '+str(val))
            if num>=val:
                # print('num into checksum: '+str(num))
                
                checksum=checksum^num
                num-=1
        # print('---------')
        val-=1
        counter+=1

    return checksum

# print(answer(17,4))
            
            
        

