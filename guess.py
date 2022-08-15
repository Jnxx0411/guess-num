import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1  #count = count + 1
	num = input('請輸入數字:')
	num = int(num)

	if num == r:
		print('終於猜對了')
		print('這次是你猜的第', count, '次') #最後會被跳掉
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這次是你猜的第', count, '次')   #寫一次不用寫3次

		

