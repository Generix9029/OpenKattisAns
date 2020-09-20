lines = 0
while True:
    prev_time = 0
    distance = 0
    lines = int(input())
    if lines == -1:
        break
    for x in range(lines):
        speed, time = input().split()
        speed, time = int(speed), int(time)
        distance += speed*(time - prev_time)
        prev_time = time
    print(f'{distance} miles')
