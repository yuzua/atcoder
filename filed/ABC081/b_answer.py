# for文を用いた全探索 シュミレーション

n=eval([*open(0)][1].replace(*' |'))
print(len(bin(n&-n))-3)

input()
n=eval(input().replace(' ','|'))
print(len(bin(n&-n))-3)