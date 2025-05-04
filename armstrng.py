# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 

# For example, take 153 (3 digits), which is narcissistic:

#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic( value ):
    sum=0
    txt=list(str(value))
    l=len(txt)
    
    for i in range(l):
        sum=(sum+(int(txt[i])**l))
        print(sum)

    if(sum==value):
        return True
    else:
        return False

print(narcissistic(7))