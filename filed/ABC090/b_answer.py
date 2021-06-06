# for文 整数の10進法表記の扱い方

# 1
A,B=map(int,input().split())
print(sum(i==i[::-1] for i in map(str,range(A,B+1))))

# 2
a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if str(i)==str(i)[::-1]:
        cnt+=1
print(cnt)