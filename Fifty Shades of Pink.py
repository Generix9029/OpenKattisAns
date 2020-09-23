n = int(input())
counter = 0
for i in range(n):
    string = input().lower()
    if 'pink' in string:
        counter += 1
    elif 'rose' in string:
        counter += 1
if counter == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(counter)
