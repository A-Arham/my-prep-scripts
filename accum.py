# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(x):
    x=str(x)
    x=x.lower()
    x=list(x)
    xlen=len(x)
    new_x=[]
    for i in range (xlen):
        c=str(x[i])
        
        cap=c.capitalize()
        new_x.append(cap)
        for j in range(i):
            new_x.append(c)
        new_x.append("-")
    


    xlen=len(new_x)
    print(xlen)
    print(xlen-1)
    del new_x[xlen-1]
    result = ''.join(new_x)
    print(result)
            
    
    #print(result)






t1="ZpglnRxqenU"

accum(t1)