N = int(input())
d = []
for i in range(N):
    d.append(input())
d.sort(reverse=True)
count = []
c = 0

for i in d:
    if i != c:
        count.append(i)
    c = i

print(len(count))