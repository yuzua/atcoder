N = int(input())
jadge = "No"

for a in range(N+1):
    for b in range(N+1-a):
        if a*4 + b*7 == N:
            jadge = "Yes"

print(jadge)