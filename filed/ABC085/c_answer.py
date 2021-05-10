# for文を用いた全探索 多重for文 工夫をし計算数を減らす

n,y=map(int,input().split())
a=[-1]*3
for i in range(n+1):
 for j in range(n-i+1):
  if 9*i+4*j+n==y/1e3:a=i,j,n-i-j
print(*a)

N, Y = map(int, input().split())
res10000 =res5000 = res1000 = -1

for x in range(N+1):
    for y in range(N+1-x):
        z = N-x-y # zは決まっているので、ループを減らして、計算量を減らす！
        if 10000*x + 5000*y + 1000*z == Y:
            res10000 = x
            res5000 = y
            res1000 = z

print(res10000, res5000, res1000)