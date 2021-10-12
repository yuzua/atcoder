import math
X = int(input())
count = 0
jadge = "Weak"
Xi = []
for i in range(4):
    s = math.floor(X % 10)
    Xi.append(int(s))
    X = X /10
Xi.reverse()
if Xi[0] == Xi[1] == Xi[2] == Xi[3]:
    pass
else:
    for i in range(3):
        if (Xi[i]+1) % 10 != Xi[i+1]:
            jadge = "Strong"
print(jadge)