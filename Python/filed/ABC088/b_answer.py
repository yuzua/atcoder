# ソート Greedy

# 1
_,s=open(c:=0)
for a in sorted(map(int,s.split())):c=a-c
print(c)

# 2
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse = True)
alice = bob = 0
for i in range(N):
    if i%2 == 0:
        alice += A[i]
    else:
        bob += A[i]

print(alice - bob)