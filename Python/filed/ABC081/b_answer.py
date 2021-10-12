# for文を用いた全探索 シュミレーション

# 1
n=eval([*open(0)][1].replace(*' |'))
print(len(bin(n&-n))-3)

# 2
input()
n=eval(input().replace(' ','|'))
print(len(bin(n&-n))-3)