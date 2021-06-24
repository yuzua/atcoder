# ソート Greedy

# 1
_,k,*l=map(int,open(0).read().split())
print(sum(sorted(l)[-k:]))

# 2
N,K = map(int,input().split())
l = list(sorted(map(int,input().split())))[::-1]
print(sum(l[:K]))