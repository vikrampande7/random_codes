def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    n = len(vectors[0])
    m = len(vectors)

    means = [sum(v)/n for v in vectors]
    cov_matrix = [[0.0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            if i<=j:
                covar = 0.0
                for k in range(n):
                    covar += (vectors[i][k]-means[i]) * (vectors[j][k] - means[j])
                covar /= (n-1)
                cov_matrix[i][j] = covar
                cov_matrix[j][i] = covar

	return cov_matrix