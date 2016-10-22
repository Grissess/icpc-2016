import cin
import combin

cases = cin.get_int()

for case in range(cases):
	coins = cin.get_int()
	cvs = [cin.get_int() for coin in range(coins)]
	target = cin.get_int()
	for ps in combin.powerset(*cvs):
		if sum(ps) == target:
			print('YES')
			break
	else:
		print('NO')
