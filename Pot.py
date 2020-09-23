lines = int(input())
sum = 0
for i in range(lines):
    num = input()
    base = int(num[:-1])
    expo = int(num[-1])
    sum += base**expo
print(sum)
