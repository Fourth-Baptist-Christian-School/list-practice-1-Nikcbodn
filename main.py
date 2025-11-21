file = open("input.txt")
contexts = file.read()
rows = contexts.split("\n")


list1 = []
list2 = []

for row in rows:
    num1, num2 = row.split("   ")
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()

difference = 0

for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])

print(difference)