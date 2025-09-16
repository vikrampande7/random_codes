def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	res = []
	for r in a:
		dp = [i1 * i2 for i1, i2 in zip(r, b)]
		res.append(sum(dp))
	return res