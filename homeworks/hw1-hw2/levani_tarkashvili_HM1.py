# # 1
#
# a = float(input("შეიყვანე რიცხვი a: "))
# b = float(input("შეიყვანე რიცხვი b: "))
#
# print(f"მიმატება: {a + b}")
# print(f"გამოკლება: {a - b}")
# print(f"გამრავლება: {a * b}")
# print(f"ჩვეულებრივი გაყოფა: {a / b}")
# print(f"მთელზე გაყოფა: {a // b}")
# print(f"ნაშთის აღება: {a % b}")
# print(f"ახარისხება: {a ** b}")

# # 2
#
# d1 = float(input("შეიყვანე d1 დიაგონალის სიგრძე: "))
# d2 = float(input("შეიყვანე d2 დიაგონალის სიგრძე: "))
#
# area = (d1 * d2) / 2
#
# print(f"რომბის ფართობია: {area}")

# # 3
#
# m = float(input("შეიყვანე m მეტრებში: "))
#
# cm = m * 100
# dc = m * 10
# ml = m * 1000
# mile = m * 0.00062
#
# print(f"სანტიმეტრებში: {cm}")
# print(f"დეციმეტრებში: {dc}")
# print(f"მილიმეტრებში: {ml}")
# print(f"მილებში: {mile}")

# #4
#
# base = float(input("შეიყვანე სამკუთხედის ფუძის სიგრძე: "))
# height = float(input("შეიყვანე სიმაღლე დაშვებული ამ ფუძეზე: "))
#
# triangle_area = 0.5 * base * height
#
# print(f"სამკუთხედის ფართობი: {triangle_area}")

# 5

a = int(input("შეიყვანე ორნიშნა რიცხვი: "))

ateuli = a // 10
erteuli = a % 10

print(f"ციფრთა ჯამი: {ateuli + erteuli}")