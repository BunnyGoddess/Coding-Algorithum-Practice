# Binary Gap  (Codility 100%)
# that, given a positive integer N, returns the length of its longest binary gap.
# return 0 if N doesn't contain a binary gap.

def solution(N):
    ans = 0
    hasZero = False
    # Find binary num
    FullBinary = bin(N)

    #cut first two char of string/print string
    binary = FullBinary[2:]
    # print(binary)
    if(binary.count('1')==1):
        return ans
    groupedZeros = binary.split('1')
    # print(groupedZeros)

    if not groupedZeros[-1] == '':
        hasZero = True

    if hasZero == True:
        del groupedZeros[-1]

    # print(groupedZeros)
    ans = len(max(groupedZeros))

    return ans

print(solution(6))
print(solution(51712))

