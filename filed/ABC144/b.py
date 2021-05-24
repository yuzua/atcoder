N = int(input())
jadge = "No"
for a in range(9):
    for b in range(9):
        if (a+1) * (b+1) == N:
            jadge = "Yes"
print(jadge)