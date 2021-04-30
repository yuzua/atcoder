# 整数の10進法表記の扱い方 for文

N, A, B = map(int, input().split())
ans = 0

def FindSumOfDigits(x):
    count = 0
    while x>0:
        count += x%10
        x = x//10

    return count

for n in range(1, N+1):
    count = FindSumOfDigits(n)
    if A<= count <=B:
        ans += n

print(ans) 


n,a,b=map(int,input().split());c=0
while n:c+=n*(a<=sum(map(int,str(n)))<=b);n-=1
print(c)