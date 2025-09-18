import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b[0]):
        return -1
    m_a = np.array(a)
    m_b = np.array(b)
    c = np.matmul(m_a, m_b)
    return c