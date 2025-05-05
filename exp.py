# # Define a function that takes in two non-negative integers a and b and returns the last decimal digit

# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1, n2):
    return pow( n1, n2, 10 )


print(last_digit(2222,33333))