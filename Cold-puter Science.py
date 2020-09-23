length = int(input())
list1 = list(map(lambda x:int(x),input().split()))
list1 = list(filter(lambda x: x < 0,list1))
print(len(list1))
