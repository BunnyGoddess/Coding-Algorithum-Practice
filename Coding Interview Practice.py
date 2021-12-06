import random
# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

# A1 = [1, 3, 6, 4, 1, 2]
# A2 = [1, 2, 3]
# A3 = [-1, -3]
#
#
# def solution(A):
#     z = list(range(1,len(A)+1))
#     try:
#         result = set(z).difference(set(A)).pop()
#     except:
#         print('here')
#         result = max(A)+1
#     return result
#
# print(solution(A1))
# print(solution(A2))
# print(solution(A3))



# #practice2
# sentence1 = "Hi all, my name is Tom...I am originally from Australia."
# sentence2 = "I need to work very hard to learn more about algorithms in Python!"
#
#
# def solution(sentence):
#     for p in "!?',;.":
#         sentence = sentence.replace(p, '')
#         print(p)
#     words = sentence.split()
#     return round(sum(len(word) for word in words) / len(words), 2)
#
#
# print(solution(sentence1))
# print(solution(sentence2))

def randomnumbergen() -> int:
    while True:
        try:
            low = int(input('Input Low Number: '))
            high = int(input('Input high number: '))
            randomnumberscreated = int(input('Input number: '))
            break
        except ValueError:
            print('Oops!  That was no valid number.  Try again...')

    low = int(low)
    high = int(high)
    randomnumberscreated = int(randomnumberscreated)
    i = 0
    random_number = 0
    running_total = 0

    while i < randomnumberscreated:
        i += 1
        random_number = random.randint(low, high)
        running_total += random_number
        print(f'{i}. Random Number: + {random_number}')
        print(f'Running Total: {running_total}\n')
    return random_number


print(randomnumbergen())
