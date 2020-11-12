num = int(input())
for i in range(num):
    g = int(input())
    list1 = []
    for x in range(g):
        h = input()
        if h not in list1:
            list1.append(h)
    print(len(list1))
