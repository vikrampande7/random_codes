def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    res = []
    for m in matrix:
        t = []
        for e in m:
            t.append(e*scalar)
        res.append(t)
    return res