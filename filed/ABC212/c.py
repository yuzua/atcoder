N, M = map(int, input().split())
A = list(input().split())
B = list(input().split())
A_SET = list(set(A))
B_SET = list(set(B))
min = 9999
for i in range(len(A_SET)):
    for j in range(len(B_SET)):
        if min > abs(int(A_SET[i]) - int(B_SET[j])):
            min = abs(int(A_SET[i]) - int(B_SET[j]))
print(min)

N, M = map(int, input().split())
A = list(input().split())
B = list(input().split())
min = 9999
for i in range(N):
    for j in range(M):
        if min > abs(int(A[i]) - int(B[j])):
            min = abs(int(A[i]) - int(B[j]))
print(min)