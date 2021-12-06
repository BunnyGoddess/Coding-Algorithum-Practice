# PairFinder

def indexcounter(array):
    count = -1
    for num in array:
        count += 1
    return count

def listFinalOutput(list):
    output = 'Numbers without a pair in array are: '
    loop = 0
    for num in list:
        output += str(num)
        loop += 1
        if loop < (indexcounter(list) + 1):
            output += ', '
    return output

def solution(A):
    A.sort()
    print('Sorted Original Array: ' + str(A))
    loop = 0
    loop1 = 1
    lastIndex = indexcounter(A)

    while lastIndex > loop1:
        lastIndex = indexcounter(A)
        try:
            if A[loop] != A[loop1]:
                loop += 1
                loop1 += 1
        except IndexError:
            A = listFinalOutput(A)
            return A
        else:
            del A[loop1]
            del A[loop]

    A = listFinalOutput(A)
    return A


A1 = [9, 3, 9, 3, 9, 7, 9]
A2 = [9, 3, 7, 3, 3, 9, 7, 9, 7]
A3 = [9, 3, 9, 3, 9, 7, 9, 10, 10, 11, 11, 11]

print(solution(A1))
print()
print(solution(A2))
print()
print(solution(A3))