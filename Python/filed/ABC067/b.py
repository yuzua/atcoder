N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
count = 0
for i in range(K):
    count += l[i]
print(count)