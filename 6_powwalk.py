import graycode

ustr = input()
xstr = input()

def to_list(s):
	assert s.startswith('{') and s.endswith('}')
	return s[1:-1].split(',')

def from_list(l):
	return '{' + ','.join(l) + '}'

u = to_list(ustr)
x = to_list(xstr)

def from_indices(idc):
	return [j for i, j in enumerate(u) if idc[i]]

def to_indices(l):
	for j in u:
		yield (1 if j in l else 0)

xi = tuple(to_indices(x))
n = 0
lim = 2 ** len(u)
seq = list(graycode.gray(len(u)))

# Find starting point
sidx = seq.index(xi)
oseq = seq[sidx:] + seq[:sidx]

for elem in oseq:
	print(from_list(from_indices(elem)))
