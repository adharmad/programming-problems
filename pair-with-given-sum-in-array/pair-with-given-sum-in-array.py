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
def findPair2(array, sumToFind):
    array.sort()

    lo = 0
    hi = len(array)
    while hi > lo:
        pass

if __name__ == '__main__':
    array = [8, 7, 2, 5, 3, 1]
    sumToFind = 10 

    #answer = findPair1(array, sumToFind)
    #print(answer)

    findPair2(array, sumToFind)
