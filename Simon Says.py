row = int(input())
for _ in range(row):
    sentence = input()
    if sentence.startswith('Simon says'):
        print(sentence[11:])
