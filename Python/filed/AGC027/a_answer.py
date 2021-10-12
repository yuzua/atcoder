# ソート Greedy

# 1
n,x,*A=map(int,open(i:=0).read().split())
for a in sorted(A):
  x-=a
  if x<0:break
  i+=1
print(i-(x>0))

# 2
n,x = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
cnt = 0
for i in range(n):
    if x - li[i] >= 0:
        cnt += 1
    x -= li[i]

if x > 0:
    print(cnt-1)
else:
    print(cnt)