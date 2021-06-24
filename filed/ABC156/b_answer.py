# for文 K進法表記の扱い方

# 1
N,K=map(int,input().split())
a=0
while K**a<=N:
  a+=1
print(a)

# 2
n,k=map(int,input().split())
count=0
while n!=0:
    n//=k
    count+=1
print(count)