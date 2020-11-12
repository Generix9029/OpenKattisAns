list1 = [1,0,0]
letters = input()
for char in letters:
    if char == 'A':
        list1[0],list1[1] = list1[1],list1[0]
    elif char == 'B':
        list1[1],list1[2] = list1[2],list1[1]
    elif char == 'C':
        list1[0],list1[2] = list1[2],list1[0]
print(list1.index(1)+1)
