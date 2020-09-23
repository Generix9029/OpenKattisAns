num = int(input())
for i in range(1,num+1):
    a, b = input().split()
    a = int(a)
    list1 = []
    for y in range(a):
        string = input()
        string = string[::-1]
        list1.append(string)
    list1.reverse()
    print('Test '+str(i))
    for n in list1:
        print(n)
