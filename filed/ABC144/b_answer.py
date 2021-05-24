# for文を用いた全探索 多重for文

# 1
print("Yes" if int(input()) in [i*j for i in range(10) for j in range(10)] else "No")

# 2
N = int(input())
if sum(a * b == N for a in range(1, 10) for b in range(1, 10)):
    print("Yes")
else:
    print("No")