N, Y = map(int, input().split())
A = B = C = -1

for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a + b + c == N and a*10000 + b*5000 + c*1000 == Y:
                A = a
                B = b
                C = c


print(A,B,C)