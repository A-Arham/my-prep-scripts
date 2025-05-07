# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]


def snail(snail_map):

    rows = []
    cols= []
    ans= []
    for row in snail_map:
        rows.append(row)

    lrow=len(rows)

    for i in range (lrow):
        ans.append(rows[0][i])
    
    for i in range (lrow):
        if(i!=0 and i!=(lrow-1)):
            ans.append(rows[i][lrow-1])
        if(i==lrow-1):
            for j in range (lrow):
                            ans.append(rows[lrow-1][lrow-1-j])
    
    for i in range(lrow-2, 0, -1):
          ans.append(rows[i][0])
          
          
          
    



        




    print(ans)


    



    return 1


array1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]


array2 = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail(array1))
