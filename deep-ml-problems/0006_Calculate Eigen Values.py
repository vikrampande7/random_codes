import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = 1
    b = -(matrix[0][0] + matrix[1][1])
    c = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis))
    eigenvalues = []

    if dis > 0:
        eigenvalues.append((-b + sqrt_val)/(2 * a))
        eigenvalues.append((-b - sqrt_val)/(2 * a))
        
    elif dis == 0: 
        eigenvalues.append((-b / (2 * a))) 

    else:
        eigenvalues.append((- b / (2 * a), + i, sqrt_val / (2 * a))) 
        eigenvalues.append((- b / (2 * a), - i, sqrt_val / (2 * a)))

	return eigenvalues