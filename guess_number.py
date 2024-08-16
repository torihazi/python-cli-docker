import random,sys

n,m=map(int, input("最小値nと最大値mを空白区切りで入力してください : ").split())

# 値の判定
if n > m :
  sys.exit("nはm以下です")

random_number = random.randint(n,m)

count = 0
while count < n:
  answer = int(input("生成された数は?:"))
  if answer < random_number:
    print("答えはそれより大きいです")
  elif answer == random_number:
    sys.exit(str(n) + "回以内に正解しました！")
  elif answer > random_number:
    print("答えはそれより小さいです")
  
  count += 1

