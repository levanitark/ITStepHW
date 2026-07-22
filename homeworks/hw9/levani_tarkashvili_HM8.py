# # 1
# def fibonachi(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
# fibonachi(10)
#
# # 2
# def anagram(str1, str2):
#     return sorted(str1.lower()) == sorted(str2.lower())
#
# print(anagram("race", "care"))

# # 3
# def factorial(n):
#     ans = 1
#     for i in range(1, n + 1):
#         ans *= i
#     return ans
#
# print(factorial(10))

# 4
def letter_count(string, char):
    return string.count(char)

print(letter_count("stringi 5 l-ti llll", "l"))
