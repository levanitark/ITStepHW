# # 1.
#
# arr = []
#
# while True:
#     symbol = input("Enter a command a/r/e: ")
#
#     if symbol == 'e':
#         break
#
#     elif symbol == 'a':
#         number_add = input("Enter a number to add: ")
#         arr.append(int(number_add))
#
#     elif symbol == 'r':
#         number_remove = input("Enter a number to remove: ")
#         if int(number_remove) in arr:
#             arr.remove(int(number_remove))
#         else:
#             print("Provided number is not in the list")
#
#     else:
#         print("Input can only be: a/r/e")
#
# print(f"Result: {arr}")

# # 2.
#
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
#
# print(f"The index of 210 is: {my_list_1.index(210)}")
#
# my_list_1[-1].append("hello")
#
# my_list_1.pop(2)
# print(f"Updated array with element on index 2 gone: {my_list_1}")
#
# my_list_2 = my_list_1.copy()
# my_list_2.clear()
#
# print(f"my_list_1: {my_list_1}")
# print(f"my_list_2: {my_list_2}")

# # 3.
#
# import re
#
# phone_input = input("Enter a phone number: ")
#
# number_format = r"^\(\d{3}\) \d{3}-\d{3}$"
#
# if re.fullmatch(number_format, phone_input):
#     print(f"Input phone number: {phone_input} is valid")
# else:
#     print("Invalid format")

