N, D = map(int, input().split())
df = []

for n in range(N):
    df_sample = []
    for d in range(D):
        df_sample.append(input())
    df.append(df_sample)

for i in range(N-1):
  for j in range(D-1):
    x = (df[i][j] + df[i+1][j]) * (df[i][j+1] + df[i+1][j+1])
    if isinstance(x, int):
      count += 1

print(count)
# 途中