def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    x = 1 / ((a*d) - (b*c))
    y = [[d, -b],[-c, a]]

    inverse = [
        [x * y[0][0], x * y[0][1]],
        [x * y[1][0], x * y[1][1]]
    ]

	return inverse