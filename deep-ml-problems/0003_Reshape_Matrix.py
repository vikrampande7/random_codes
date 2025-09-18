import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return []
    reshaped_matrix = [] 
    merged = []
    for m in a:
        merged.extend(m)
    for i in range(0, len(merged)-1, new_shape[1]):
        reshaped_matrix.append(merged[i:i+new_shape[1]])
	return reshaped_matrix