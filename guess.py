# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "你猜對了！"
# 猜錯的話 要告訴他 比答案大/小

import random
x = random.randint(1, 100)

while True:
	num = input('請猜數字： ')
	if int(num) == x:
		print('你猜對了！')
		break
	elif int(num) > x:
		print('比答案大')
	elif int(num) < x:
		print('比答案小')



