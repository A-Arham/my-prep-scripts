# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...


def friend(x):
    x=list(x)
    lenx=len(x)
    friends=[]
    for i in range(lenx):
        ind=x[i]
        ind=list(ind)
        l_ind=len(ind)
        if(l_ind==4):
            friends.append(x[i])


    print(friends)




names=['Arham','Aliza','Abdullah','Ryan','Yous']

friend(names)
