num = int(input())
list1 = []
for i in range(num):
    list1.append(int(input()))
list1.sort()
remainder = num%3
total = sum(list1)
for i in list1[remainder::3]:
    total -= i
print(total)
