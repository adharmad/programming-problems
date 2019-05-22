# Given an unsorted array, find a pair with the given sum
# eg - Given
# array = [8, 7, 2, 5, 3, 1]
# sum = 10
# Answer should be:
#   indices 0 and 3 (8+2 = 10)
#   or
#   indices 1 and 4 (7+3 = 10)

# Naive solution
# Iterate over the arrays and compute sums of all pairs until
# we find the answer we are looking for
# O(n*n) time complexity
# O(1) space complexity
def findPair1(array, sumToFind):
    for i in range(len(array)-1):
        for j in range(i, len(array)):
            currSum = array[i] + array[j]
            if currSum == sumToFind:
                return (i, j)

    return (-1, -1)

# Sort the array and traverse it from beginning and end
# progressively increasing the begin index and end index until
# We hit the correct sum
# Here we cannot return the original indices but can return the
# numbers that add up to the required sum
def findPair2(array, sumToFind):
    array.sort()

    lo = 0
    hi = len(array)-1
    while hi > lo:

        currSum = array[lo] + array[hi]
        if currSum == sumToFind:
            return (array[lo], array[hi])
        elif currSum > sumToFind:
            hi -= 1
        elif currSum < sumToFind:
            lo += 1

    return (-1, -1)

# Keep a dict of elem -> (sumToFind-elem)
# If the value of the dict exists as a key then you have found the answer
def findPair3(array, sumToFind):
    d = {}

    for elem in array:
        d[elem] = sumToFind-elem

    for k, v in d.items():
        if v in d:
            return (k, v)

    return (-1, -1)

if __name__ == '__main__':
    array = [8, 7, 2, 5, 3, 1]
    sumToFind = 12 

    #answer = findPair1(array, sumToFind)
    #print(answer)

    #answer = findPair2(array, sumToFind)
    #print(answer)

    answer = findPair3(array, sumToFind)
    print(answer)
