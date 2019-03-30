# solution to pascal's triangle via recursion
# The goal is to print out pascal's triangle. Use recursion to compute
# the values
#
# Pascal's triangle is as follows:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
#
# Pascal's triangle's recursion relation can be represented as
# P(i, j) = P(i, j-1) + P(i-1, j-1)
# i = column
# j = row 

def pascal(i, j):
    # If the column does not exist, value is 0
    if i > j:
        return 0
    # Common cases - first and second rows are all 1's
    elif j == 1 or j == 2:
        return 1
    # first column is always 1
    elif i == 1:
        return 1
    else:
        return pascal(i, j-1) + pascal(i-1, j-1)

def main():
    s = ''

    for j in range(1, 10):
        for i in range(1, j+1):
            pij = pascal(i, j)
            s += str(pij) + ' '
            #print("pascal", i, j, " = ", pij)
        s += '\n'

    print(s)


if __name__ == '__main__':
    main()
