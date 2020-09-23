sum = 0
lines = int(input())
for i in range(lines):
    string1 = input()
    list1 = string1.split()
    x, y = float(list1[0]), float(list1[1])
    sum += x*y
print(sum)
