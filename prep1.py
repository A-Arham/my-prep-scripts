import numpy as np

def checker(arr1, arr2):
    comm = []
    for i in arr1:
        for j in arr2:
            if i == j:
                comm.append(i)
    return len(comm)



def test_checker():
    # Test 1
    answer = checker([1, 2, 3], [4, 5, 6])
    if answer == 0:
        print("Test 1: Passed")
    else:
        print("Test 1: Failed, got", answer)

    # Test 2
    answer = checker([1, 2, 3], [3, 4, 5])
    if answer == 1:
        print("Test 2: Passed")
    else:
        print("Test 2: Failed, got", answer)

    # Test 3
    answer = checker([1, 2], [1, 2])
    if answer == 2:
        print("Test 3: Passed")
    else:
        print("Test 3: Failed, got", answer)

    # Test 4
    answer = checker([-1, -2], [-2, -3])
    if answer == 1:
        print("Test 4: Passed")
    else:
        print("Test 4: Failed, got", answer)

    # Test 5
    answer = checker([], [])
    if answer == 0:
        print("Test 5: Passed")
    else:
        print("Test 5: Failed, got", answer)

# Run the tests
test_checker()


