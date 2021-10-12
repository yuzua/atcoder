N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
count = 0
for i in range(N):
    count += a[i+N]
print(count)
# 途中