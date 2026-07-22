# # 1
# int_list = [10, 20, 30, 40]
#
# def insertion(num):
#     int_list.append(num)
#
# insertion(50)
# print(int_list)

# # 2
# def return_sum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
# test_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# print(return_sum(test_list))

# # 3
# gl_str = "Global"
#
# def create_local():
#     gl_str = "Local"
#     return gl_str
#
# print(create_local())
# print(gl_str)

# 4
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     last_digit = n % 10
#     rest = n // 10
#     total = last_digit + sum_of_digits(rest)
#     return total
#
# print(sum_of_digits(12345))

# 5
def reverse(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse(text[:-1])

print(reverse("Hello"))
