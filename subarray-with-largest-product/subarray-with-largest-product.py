# Find the subarray with the largest product in an array having
# both positive and negative integer elements
# eg - 
# array = [1, 0, -5, 3, -9, 2, 2, 0, -4, -10, 0, 5, 6, -4, -2, 1]
# answer: [-5, 3, -9, 2, 2]

from functools import reduce

# Naive solution
# Inspect arrays of all lengths keeping track of maximum product and the 
# subarray
def subArrayWithLargestProduct(array):
    subarray = []
    maxProduct = 0

    subArrayLength = len(array) # start with the complete array
    
    for tmplen in range(subArrayLength, 0, -1):
        for startIdx in range(len(array)-tmplen+1):
            tmparray = array[startIdx:startIdx+tmplen]
            tmpsum = reduce((lambda x, y: x * y), tmparray)

            if tmpsum > maxProduct:
                maxProduct = tmpsum
                subarray = tmparray

    return subarray

if __name__ == '__main__':
    array = [1, 0, -5, 3, -9, 2, 2, 0, -4, -10, 0, 5, 6, -4, -2, 1]

    subarray = subArrayWithLargestProduct(array)
    print(subarray)
