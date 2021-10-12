s = input()
t = input()

slist = sorted([i for i in s])
tlist = sorted([j for j in t], reverse=True)

ssorted = "".join(slist)
tsorted = "".join(tlist)

if tsorted > ssorted:
  print("Yes")
else:
  print("No")
