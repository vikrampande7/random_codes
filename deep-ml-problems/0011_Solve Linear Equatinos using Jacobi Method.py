import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = [0 for _ in range(len(b))]
    for _ in range(n):
        x_old = x[:]
        for i in range(0, len(A)):       
            total = 0
            for j in range(0, len(A[0])):
                if i == j:
                    continue
                total += (A[i][j] * x_old[j])
            x[i] = (1 / A[i][i]) * (b[i] - total)
	return x