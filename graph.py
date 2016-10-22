import combin

def is_independent(v, e, s):
	marks = {i: (i in s) for i in v}
	for edge in e:
		if edge[0] == edge[1]:
			continue
		if marks[edge[0]] and marks[edge[1]]:
			return False
	return True

def weighted_is(vw, e):
	best_set = None
	best_weight = None
	v = vw.keys()
	for s in combin.powerset(*v):
		if not is_independent(v, e, s):
			continue
		weight = sum(vw[i] for i in s)
		if best_set is None or weight > best_weight:
			best_set = s
			best_weight = weight
	return set([] if best_set is None else best_set), 0 if best_weight is None else best_weight
