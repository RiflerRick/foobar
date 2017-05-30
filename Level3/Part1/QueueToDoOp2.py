def answer(start, length):

    counter=length

    num=start
    
    checkSum=0

    while counter>0:
        # print('num: '+str(num))
        # print('counter: '+str(counter))
        if num%2==0:
            
            if counter%4==3:
                rowCheckSum=num+counter
            elif counter%4==2:
                rowCheckSum=1
            elif counter%4==1:
                rowCheckSum=num+counter-1
            else:
                rowCheckSum=0
            checkSum=checkSum^rowCheckSum
        else:
            valuesToCheck=counter-1
            if valuesToCheck%4==3:
                rowCheckSum=num+counter
            elif valuesToCheck%4==2:
                rowCheckSum=1
            elif valuesToCheck%4==1:
                rowCheckSum=num+counter-1
            else:
                rowCheckSum=0
            checkSum=checkSum^rowCheckSum^num

        # print('checkSum: '+str(checkSum))
        # print('------------')
        num+=length
        counter-=1

    return checkSum

# print(answer(17,4))

            


