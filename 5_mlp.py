import cin
import combin

def det(a, b, c, d):
	return (a * b - c * d)

def slv_a(p1, p2):
	return -det(p1[1], p2[2], p2[1], p1[2]) / det(p1[0], p2[1], p2[0], p1[1])

def slv_b(p1, p2):
	return det(p1[0], p2[2], p2[0], p1[2]) / det(p1[0], p2[1], p2[0], p1[1])

cases = cin.get_int()

for case in range(cases):
	trips = cin.get_int()
	pts = [(cin.get_int(), cin.get_int(), cin.get_int()) for trip in range(trips)]
	best_err = None
	best_ab = None
	for x, y in combin.choose(pts, 2):
		try:
			a, b = slv_a(x, y), slv_b(x, y)
		except ZeroDivisionError:  # Degenerate!
			continue
		err = 0.0
		for pt in pts:
			err += abs(pt[2] - (a * pt[0] + b * pt[1]))
		if best_err is None or err < best_err:
			best_ab = (a, b)
			best_err = err
	if best_ab is None:
		best_ab = (0.0, 0.0)
	print('%0.2f %0.2f' % best_ab)
