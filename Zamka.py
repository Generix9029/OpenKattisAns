l = int(input())
d = int(input())
x = int(input())
def helper(h):
    sum = 0
    for num in str(h):
        sum += int(num)
    return sum

list1 = []
for num in range(l,d+1):
    f = helper(num)
    if f == x:
        list1.append(num)
print(min(list1))
print(max(list1)
