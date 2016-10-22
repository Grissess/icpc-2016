import cin
import graph

cases = cin.get_int()

for case in range(cases):
	people = cin.get_int()
	famsz = {}
	bosses = []
	for person in range(people):
		eid = cin.get_int()
		fsz = cin.get_int()
		bid = cin.get_int()
		famsz[eid] = fsz
		if bid != -1:
			bosses.append((eid, bid))

	s, w = graph.weighted_is(famsz, bosses)
	print( w)
