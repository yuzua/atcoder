# N = int(input())
# S = ["A"]
# ball = 1
# while ball < N:
#     if ball*2 <= N:
#         ball *= 2
#         S.append("B")
#     else:
#         number = N - ball
#         if number > 10:
#             S.append("A" * 10)
#             number -= 10
#         else:
#             S.append("A" * number)
#         break
# print("".join(S))

N = int(input())
S = ["A"]
ball = 1
while True:
    if ball*2 <= N:
        S.append("B")
        ball *= 2
    else:
        S.append("A" * (N-ball))
        break
print("".join(S))