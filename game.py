# number guesing game
# generate random number by random
# let user to shoot the number by input
# if the answer is correct => print gotcha
# if the answer is wrong => bigger or smaller
import random
x = input('please input the maximum number of the game scope: ')
x = int(x)
y = input('please input the minimum number of the game scope: ')
y = int(y)
r = random.randint(y, x)
i = 10 # i = 猜測次數
print('you have maximun 10 chances to shoot the number.')
while i > 0:
	print('chances left: ', i) # 盡量不要把這句寫在if架構裡面，會導致重複性太高
	i -= 1 # x = x + 1等同於x += 1； x = x - 1等同於x -= 1
	a = input('please guess the number: ')
	a = int(a) # r是integer，a也要是integer才能比較
	if a == r:
		print('gotcha!')
		break
	elif a > r:
		print('too large!')
	else:
		print('too small!')
else:
	print('you are running out oh chance!')