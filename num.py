def pr_factor(n):
	r = []
	z = 2
	sqrn = n ** 0.5
	while n != 1 and z < sqrn:
		if n % z == 0:
			n = n // z
			r.append(z)
			z = 2
		else:
			z += 1
	return r + ([] if n == 1 else [n])
