list1 = []
for i in range(3):
    list1.append([int(x) for x in input().split()])
if (list1[0][0]-list1[1][0])**2 + (list1[0][1]-list1[1][1])**2 > (list1[0][0]-list1[2][0])**2 + (list1[0][1]-list1[2][1])**2:
    diag1 = list1[0]
    diag2 = list1[1]
    oop = list1[2]
elif (list1[0][0]-list1[1][0])**2 + (list1[0][1]-list1[1][1])**2 == (list1[0][0]-list1[2][0])**2 + (list1[0][1]-list1[2][1])**2:
    diag1 = list1[1]
    diag2 = list1[2]
    oop = list1[0]
else:
    diag1 = list1[0]
    diag2 = list1[2]
    oop = list1[1]
#print(diag1,diag2,oop)
x = diag1[0]+diag2[0]-oop[0]
y = diag1[1]+diag2[1]-oop[1]
print(x, y)
