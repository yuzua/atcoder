def has_duplicates(seq):
    return len(seq) != len(set(seq))

N = int(input())
list = []
for i in range(N):
    list.append(input())
print("Yes" if has_duplicates(list) == True else "No")