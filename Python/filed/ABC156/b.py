import math, itertools
N, K = map(int, input().split())
count = []
for _ in itertools.count():
    if N > 0:
        count.append(N % K)
        N = math.floor(N / K)
    else:
        break
print(len(count))