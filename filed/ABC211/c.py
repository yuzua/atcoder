from itertools import accumulate

m = 1000000007
S = input()
S = S[::-1]
n = len(S)

a = [1] * n
for c in reversed('chokudai'):
    b = [0] * n
    for i in range(n):
        if S[i] != c:
            continue
        b[i] = a[i] % m
    a = list(accumulate(b))
print(a[-1] % m)