def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = []
	for i in range(0, len(a[0])):
		t = []
		for m in a:
			t.append(m[i])
		b.append(t)
	return b