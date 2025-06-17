import random
import sys

# 最小値
n = input('最小値を入力してください: ')

# 最大値
m = input('最大値を入力してください: ')

# 最小値が最大値より小さいかチェック
if n > m:
    print('最小値は最大値より小さい必要があります。')
    sys.exit(1)

# 入力値が数値であるかチェック
if not n.isdigit() or not m.isdigit():
    print('数値を入力してください。')
    sys.exit(1)

# 入力値が負の数でないかチェック
if int(n) < 0 or int(m) < 0:
    print('負の数は入力できません。')
    sys.exit(1)

# 最小値と最大値が同じでないかチェック
if int(n) == int(m):
    print('最小値と最大値は異なる必要があります。')
    sys.exit(1)

# ランダムな数を生成
random_number = random.randint(int(n), int(m))

for i in range(int(n), int(m) + 1):
    guess_number = input('予想する数を入力してください: ')
    if int(guess_number) < random_number:
        print('もっと大きい数です。')
    elif int(guess_number) > random_number:
        print('もっと小さい数です。')
    else:
        print('正解です！')
        break
else:
    print('残念！正解は', random_number, 'でした。')

print('ゲームを終了します。')