import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A = np.array(A, dtype=float)
    T = np.array(T, dtype=float)
    S = np.array(S, dtype=float)

    try:
        T_inv = np.linalg.inv(T)
        S_inv = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        return -1

    transformed_matrix = T_inv @ A @ S
    return transformed_matrix.tolist()