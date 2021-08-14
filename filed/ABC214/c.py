# できていない
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
ST = []
jadge = []
count = 0
sum = T[0]
for i in range(len(S)):
    sum += S[i]
    ST.append(sum)
# while True:
#     if len(jadge) >= N:
#         break
#     else:
#         if T[n] <= ST[m]:
#             jadge.append(T[n])
#             n+=1
#         elif T[n] == ST[n-1]:
#             jadge.append(T[n])
#             n+=1
#             m+=1
#         else:
#             jadge.append(ST[m])
#             m+=1
for i in range(len(T)):
    if i == 0:
        jadge.append(T[i])
    else:
        jadge.append(min(T[i],ST[i-1]))
for i in range(N):
    print(jadge[i])
