N, L = map(int, input().split())
list = []
for i in range(N):
    list.append(input())
list = sorted(list)
list_join = (''.join(list))
print(list_join)