N = int(input())
t = [0]
x = [0]
y = [0]

for i in range(N):
    T, X, Y = map(int, input().split())
    t.append(T)
    x.append(X)
    y.append(Y)

for i in range(N):
    loop = t[i] - t[i+1]
    


print(t, x, y)