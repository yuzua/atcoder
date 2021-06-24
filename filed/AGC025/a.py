import math
N = int(input())
min = 9999
for a in range(1,N):
    b = N-a
    count = 0
    for _ in range(len(str(a))):
        count += a % 10
        a = math.floor(a / 10)
    for _ in range(len(str(b))):
        count += b % 10
        b = math.floor(b / 10)
    if min > count:
        min = count
print(min)

