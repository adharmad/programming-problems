# Find the subarray with the largest sum in an array having
# both positive and negative integer elements
# eg - 
# array = [1, 0, -5, 3, -9, 2, 2, 3, -10, 5, 6, -4, -2, 1]
# answer: [5, 6]


# Naive solution
# Inspect arrays of all lengths keeping track of maximum sum and the 
# subarray
def subArrayWithLargestSum(array):
    subarray = []
    maxSum = 0

    subArrayLength = len(array) # start with the complete array
    
    for tmplen in range(subArrayLength, 0, -1):
        for startIdx in range(len(array)-tmplen+1):
            tmparray = array[startIdx:startIdx+tmplen]
            tmpsum = sum(tmparray)

            if tmpsum > maxSum:
                maxSum = tmpsum
                subarray = tmparray

    return subarray

if __name__ == '__main__':
    array = [1, 0, -5, 3, -9, 2, 2, 3, -10, 5, 6, -4, -2, 1]

    subarray = subArrayWithLargestSum(array)
    print(subarray)
