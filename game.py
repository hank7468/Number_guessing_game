# number guesing game
# generate random number by random
# let user to shoot the number by input
# if the answer is correct => print gotcha
# if the answer is wrong => bigger or smaller
import random
r = random.randint(1, 1000)
i = 10 # i = 猜測次數
while i > 0:
	print('you have', i, 'opportunities.')
	i = i - 1
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