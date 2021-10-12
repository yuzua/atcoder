# 同一判定
# set()で値をsetオブジェクトとして作成,addすることにより同じ文字は追加されず,違う文字のみ追加されるため判定文字数の4を超えた場合"No"

S_set = set()
for _ in range(4):
    S = input()
    S_set.add(S)

print('Yes' if len(S_set) == 4 else 'No')