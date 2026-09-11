# # 1
#
# num_list = [44, 23, 11, 8, 20, 56, 33, 55]
#
# input = int(input("Enter a number: "))
#
# if input in num_list:
#     print("The number is in list")
# else:
#     print("The number not in list")

# # 2
#
# input = int(input("Enter an integer: "))
#
# if input % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# # 3
#
# st1 = "string"
# st2 = "string"
#
# if st1 is st2:
#     print("Same object")
# else:
#     print("Different object")

# 4

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

input = int(input("Input a number: "))

if input > num_list[2] and input < num_list[-1]:
    print("More than list elements")
elif input == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")