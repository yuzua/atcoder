X, Y = map(int, input().split("."))
if Y >= 3 and Y <= 6:
    print(X)
elif Y >= 0 and Y <= 2:
    print(str(X)+"-")
else:
    print(str(X)+"+")