N = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0
 
for i in range(N):
    for j in range(i):
        for k in range(j):
            if (L[i] != L[j] and L[j] != L[k] and L[k] + L[j] > L[i]):
                count += 1
print(count)