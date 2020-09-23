num = int(input())
while num > 9:
    list1 = list(str(num))
    counter = 0
    for i in list1:
        if i == '0':
            counter += 1
    for i in range(counter):
        list1.remove('0')
    num = 1
    for i in list1:
        num *= int(i)
print(num)
