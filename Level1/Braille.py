def answer(plaintext):
    """
    brCodes is a dictionary that encodes 
    all the characters in the english alphabet into 
    braille codes: a -> 0, b -> 1 and so on
    """
    brCodes={}
    brCodes[0]='100000'
    brCodes[1]='110000'
    brCodes[2]='100100'
    brCodes[3]='100110'
    brCodes[4]='100010'
    brCodes[5]='110100'
    brCodes[6]='110110'
    brCodes[7]='110010'
    brCodes[8]='010100'
    brCodes[9]='010110'
    #  first 10 characters encoded
    for i in range(10, 20):
        sub=brCodes[i-10]
        brCodes[i]=sub[:2]+'1'+sub[3:]
    check=0
    for i in range(20, 26):
        if i==22:
            sub=brCodes[9]
            brCodes[i]=sub[:5]+'1'
            check=1
        else:
            if check==0:
                sub=brCodes[i-20]
            else:
                sub=brCodes[i-21]
            brCodes[i]=sub[:2]+'1'+sub[3:5]+'1'
    # all 26 alphabets encoded in braille
    code=''
    # DEBUG:

    # for i in brCodes:
        # print(str(i)+":"+str(brCodes[i]))

    for ch in plaintext:
        if ch.isupper():
            # the character is upper case and hence
            # the braille for that must be included
            code=code+'000001'+brCodes[ord(ch)-65]
        elif ch.isspace():
            # the character is a space 
            code=code+'000000'
        else:
            code=code+brCodes[ord(ch)-97]
    return code
def main():
    ans=answer('The quick brown fox jumped over the lazy dog')
    # check:
    a='000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
    if a==ans:
        print("yup")
    else:
        print("ans: "+ans)
        index=0
        # for i in ans:
            # if i!= a[index]:
                # print(int(index/6))
            # index+=1 
if __name__=="__main__":
    main()