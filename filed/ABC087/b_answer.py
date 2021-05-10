# for文を用いた全探索 多重for文

# 1
A, B, C, X = [int(input()) for _ in range(4)]
print([500*a + 100*b + 50*c for c in range(C+1) for b in range(B+1) for a in range(A+1)].count(X))

# 2
a,b,c,x=eval('int(input())+1,'*4);print(sum(c>x/50-I//b*10-I%b*2>0for I in range(a*b)))