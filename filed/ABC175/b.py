# N = int(input())
# L = list(map(int,input().split()))
# L.sort()
# count = 0
# for i in range(len(L)-2):
#     print("i = "+str(i))
#     for j in range(N-i):
#         j = j+i
#         print("j = "+str(j))
#         for k in range(N-j):
#             k = k+j
#             print("k = "+str(k))
#             if L[i] < L[j] < L[k] and L[i] != L[j] != L[k]:
#                 count += 1
#                 print("if i = "+str(L[i]))
#                 print("if j = "+str(L[j]))
#                 print("if k = "+str(L[k]))
# print(count)

# # 4 7 9
# # 4 5 7
# # 4 7 9
# # 4 5 7
# # 5 7 9

N = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0
 
for i in range(N):
    print("i = "+str(L[i]))
    for j in range(i):
        print("j = "+str(L[j]))
        for k in range(j):
            print("k = "+str(L[k]))
            if (L[i] != L[j] and L[j] != L[k] and L[k] + L[j] > L[i]):
                print("if i = "+str(L[i]))
                print("if j = "+str(L[j]))
                print("if k = "+str(L[k]))
                count += 1
print(count)