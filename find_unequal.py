# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr):

    n=0
    len1=len(arr)-1
    for i in range(len1):
        if(arr[i]-arr[i-1]!=0 and arr[i+1]-arr[i]!=0):
            print(arr[i])
            n=arr[i]

    c=arr[len1]-arr[len1-1]
    if(c!=0):
        n=arr[len1]

    return n   # n: unique number in the array


in1=[ 1, 1, 1, 1, 1, 20 ]
in2=[ 0, 0, 0.55, 0, 0 ]
in3=[ 7, 7, 7, 7, 7, 7, 6, 7 ]
find_uniq(in3)