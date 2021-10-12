# わからん
import math
N, D = map(int, input().split())
df = []

for n in range(N):
    df_sample = []
    for d in range(D):
        df_sample.append(input())
    df.append(df_sample)

for i in range(N-1):
  for j in range(D-1):
    x = math.sqrt(((abs(df[i][j] + df[i+1][j])**2)) + (abs((df[i][j+1] + df[i+1][j+1]))**2))
    if isinstance(x, int):
      count += 1

print(count)