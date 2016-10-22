import cin
import num
import combin

cases = cin.get_int()

for case in range(cases):
	n, m = cin.get_int(), cin.get_int()
	pr = num.pr_factor(n)
	prp = sum([[(p**i) for i in range(1, n)] for p in pr], [])
	print(prp)
	for ps in combin.powerset(pr):
		if not ps:
			continue

