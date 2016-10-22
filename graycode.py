def gray(bits):
	if bits == 1:
		yield from ((0,), (1,))
		return
	if bits == 2:
		yield from ((0, 0), (0, 1), (1, 1), (1, 0))
		return
	parity = False
	lbits = 2 * ((bits - 1) // 2)
	fwd = list(gray(lbits))
	for leftseq in gray(bits - lbits):
		for rightseq in (reversed(fwd) if parity else fwd):
			yield leftseq + rightseq
		parity = not parity
