# # 1.
# string_input = input("შეიტანე მიმდევრობა: ")
# unique_set = set(string_input.split())
# print(unique_set)

# # 2.
# string_input = input("შეიტანე მიმდევრობა: ")
# frozen_set = frozenset(string_input.split())
# print(frozen_set)

# # 3.
# SET_A = {11, 22, 33}
# SET_B = {5, 16, 27, 60}
#
# combined_tuple = tuple(SET_A.union(SET_B))
# print(combined_tuple)

# 4.
# string_input = input("შეიტანე მიმდევრობა: ")
# input_tuple = tuple(string_input.split())
# unique_list = list(set(input_tuple))
# print(unique_list)

# 5.
# g_names = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for name, age in g_names:
#     print(f"Name: {name}, Age: {age}")

# 6.
names_a = ["Irakli", "Giorgi", "Nona", "Oto"]
names_b = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

overlap = list(set(names_a).intersection(set(names_b)))
print(overlap)