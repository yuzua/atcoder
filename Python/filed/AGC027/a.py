N, x = map(int, input().split())
list = list(map(int, input().split()))
list.sort()
count = 0
if x == sum(list):
    count = N
elif x > sum(list):
    count = N-1
else:
   for i in range(N):
    x -= list[i]
    if x >= 0:
        count += 1
    else:
        break
print(count)