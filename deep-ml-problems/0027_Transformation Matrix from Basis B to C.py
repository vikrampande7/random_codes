import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    _B = np.array(B)
    _C = np.array(C)
    _C_INV = np.linalg.inv(_C)
    P = _C_INV @ B
	return P