list1 = list(input().split())
list1 = [int(x) for x in list1]
list1.sort()
string = input()
return_string = ''
for i in string:
    if i == 'A':
        return_string += str(list1[0]) + ' '
    elif i == 'B':
        return_string += str(list1[1]) + ' '
    elif i == 'C':
        return_string += str(list1[2]) + ' '
print(return_string.rstrip(' '))
