import math
# proměnné a řetězce
jmeno = "Luky"
vek = 23
print(f"jmenuji se {jmeno} a je mi {vek} let")

numbers = [8, 7, 3, 4, 5]

numbers.append(7)
numbers.sort()
print(f"seřazený seznam: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")
# Slovníky a množiny

student = {}
student ["vek"] = 23
student ["jmeno"] = "Luky"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print(f"Student: {student['jmeno']}, věk: {student['vek']}, předměty: {student['predmety']}")