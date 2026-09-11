# 1.
#
# string_input = input("Enter a string: ")
# print(f"String in UFT-8: {string_input.encode('utf-8')}")

# 2.
#
# string_input = input("Enter a string: ")
# new_string = string_input.strip().lower().replace("python", "Python") + "Python"
#
# print(f"transformed string: {new_string}")

# 3.
#
# string_input = input("Enter a string: ")
#
# new_string = string_input[:len(string_input) // 2]
# print(f"first half: '{new_string}'")

# 4.
# import string
#
# string_input = input("Enter a string: ")
#
# at_least_letter = any(c in string.ascii_letters for c in string_input)
# at_least_one_digit = any(c in string.digits for c in string_input)
#
# if at_least_letter and at_least_one_digit and string_input.isalnum():
#     print("String is valid")
# else:
#     print("string is invalid")

# # 5.
#
# string_input = input("Enter a string: ")
#
# string_bytes = string_input.encode('utf-8')
# print(f"String in bytes : {string_bytes}")
#
# print(f"Back to string: {string_bytes.decode('utf-8')}")
