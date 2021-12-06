# Find Missing Number Algorithm  (Big O Notation 100% Percent on Codility)

# An array A consisting of N different integers is given. The array contains exactly one element is missing.
# Your goal is to find that missing element. That, given an array A, returns the value of the missing element.
# For example, given array A such that:
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# The function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

def solution(A):
    i = 0
    nplus = 0
    while i <= len(A):
        i += 1
        nplus += i
    arraySum = sum(A)
    ans = nplus - arraySum
    return ans


A = [1, 2, 3, 5]
A1 = [1, 2, 3, 4, 5, 7, 8, 9]
A2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

print(solution(A))
print(solution(A1))
print(solution(A2))