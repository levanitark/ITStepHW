# # 1
# def zip_it(list1, list2):
#     result = []
#     for pair in zip(list1, list2):
#         string_pair = str(pair)
#         result.append(string_pair)
#     return result
#
# print(zip_it([1, 2, 3], ['a', 'b', 'c']))

# 2
# from functools import reduce
#
# def product(numbers):
#     try:
#         return reduce(lambda x, y: x * y, numbers)
#     except TypeError:
#         return "Error: input can only be a number list"
#
# print(product([1, 2, 3, 4, 5]))

# # 3
# odd_elements = lambda numbers: [x for x in numbers if x % 2 != 0]
#
# print(odd_elements([1, 2, 3, 4, 5, 6, 7]))

# 4
def end_by_filter(strings, ending):
    try:
        return list(filter(lambda string: string.endswith(ending), strings))
    except TypeError:
        return "Error: Invalid data type"
    except Exception as e:
        return f"unexpected error occurred: {e}"

print(end_by_filter(['hello', 'world', 'coding', 'nod'], 'ing'))