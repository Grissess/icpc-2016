import cin

class Board(object):
	def __init__(self, sx, sy):
		self.board = [[False for i in range(sy)] for j in range(sx)]

	def mark(self, x, y):
		old = self.get(x, y)
		self.board[x][y] = True
		return not old

	def in_bounds(self, x, y):
		return (0 <= x < len(self.board) and 0 <= y < len(self.board[0]))
	
	def get(self, x, y):
		if not self.in_bounds(x, y):
			return False
		return self.board[x][y]

	def points(self):
		for lx in range(len(self.board)):
			for ly in range(len(self.board[0])):
				yield lx, ly

	def mark_reachable_from(self, x, y, dx, dy):
		self.mark(x, y)
		spec = (
			(dx, dy), (dy, dx),
			(-dx, dy), (-dy, dx),
			(dx, -dy), (dy, -dx),
			(-dx, -dy), (-dy, -dx),
		)
		while True:
			quiesced = True
			for lx, ly in self.points():
				if self.get(lx, ly):
					for tx, ty in spec:
						if not self.in_bounds(lx + tx, ly + ty):
							continue
						quiesced = quiesced and not self.mark(lx + tx, ly + ty)
			if quiesced:
				break

	def is_covered(self):
		return all(all(col) for col in self.board)

	def print_marked(self):
		for lx in range(len(self.board)):
			for ly in range(len(self.board[0])):
				if self.get(lx, ly):
					print('*', end=' ')
				else:
					print('-', end=' ')
			print()

	def get_open_pt(self):
		for lx, ly in self.points():
			if not self.get(lx, ly):
				return lx, ly
		return None  # Explicit

cases = cin.get_int()

for case in range(cases):
	b = Board(cin.get_int(), cin.get_int())
	dx, dy = cin.get_int(), cin.get_int()
	if (dx, dy) in ((0, 1), (1, 0)):
		print(1)
		continue
	frogs = 0
	while not b.is_covered():
		frogs += 1
		startx, starty = b.get_open_pt()
		b.mark_reachable_from(startx, starty, dx, dy)
		#print('Iter', frogs)
		#b.print_marked()
	print(frogs)
