MOD = 10 ** 9 + 7


def main():
    from collections import Counter

    S = input()
    T = '*chokudai'  # 0文字目は英小文字でない適当な記号にします
    dp = Counter()
    dp['*'] = 1
    for char in S:
        if char in T:
            char_prev = T[T.index(char) - 1]  # charの前の文字、iの前はa、cの前は*
            dp[char] += dp[char_prev]
            dp[char] %= MOD
    print(dp['i'])


if __name__ == '__main__':
    main()