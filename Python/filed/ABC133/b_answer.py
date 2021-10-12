# for文を用いた全探索 多重for文

# 1
n,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        tmp=0
        for k in range(d):
            tmp+=(arr[j][k]-arr[i][k])**2
        tmp=tmp**0.5
        if tmp==int(tmp):
            ans+=1
print(ans)

# 2
from numpy import*
n,*x=[int32(t.split())for t in open(0)]
print(sum(triu([linalg.norm(i-x,2,1)%1==0 for i in x],1)))