def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

    if mode == 'row':
        for m in matrix:
            mn = sum(m) / len(m)
            means.append(mn)
            
    if mode == 'column':
        for i in range(0, len(matrix[0])):
            s = []
            for m in matrix:
                s.append(m[i])
            means.append(sum(s)/len(s))
    
    return means