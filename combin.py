def permute(*choices):
	if choices:
		for elem in choices[0]:
			for right in permute(*choices[1:]):
				yield (elem,) + right
	else:
		yield ()

def powerset(*elems):
	if elems:
		for right in powerset(*elems[1:]):
			yield right
			yield (elems[0],) + right
	else:
		yield ()

def choose(s, n):
	if n == 1:
		for elem in s:
			yield (elem,)
	else:
		for idx, elem in enumerate(s):
			rset = s[idx+1:]
			if rset:
				for right in choose(rset, n-1):
					yield (elem,) + right

def choose_all(s, n):
	if n == 1:
		for elem in s:
			yield (elem,)
	else:
		for idx, elem in enumerate(s):
			for right in choose(s, n-1):
				yield (elem,) + right
