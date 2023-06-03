import math

# Get two probabilities
py = 9/14
pn = 5/14

# Entropy formula y*log(y)
hy = - py * math.log2(py) - pn * math.log2(pn)

print(f"Entropy is: {hy}")


#%%
