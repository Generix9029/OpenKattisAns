import string
n = int(input())
for i in range(n):
    string_list = [x for x in string.ascii_lowercase]
    passin_string = input().replace(' ','')
    for i in passin_string:
        if i.lower() in string_list:
            string_list.remove(i.lower())
    if string_list == []:
        print('pangram')
    else:
        return_string = ''
        for i in string_list:
            return_string += i
        print('missing '+return_string)
