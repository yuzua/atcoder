N =int(input())
a = list(map(int, input().split()))
count = 0
A = 0
B = 0
a.sort(reverse=True)
for i in a:
    if count % 2 == 0:
        A += i
        count += 1
    else:
        B += i
        count += 1
print(A-B)