S = []
Sx = ["H" , "2B" , "3B" , "HR"]
jadge = "Yes"
for i in range(4):
    S.append(str(input()))
if sorted(S) != sorted(Sx):
    jadge = "No"
print(jadge)