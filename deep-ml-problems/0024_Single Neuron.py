import math
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    out = []
    for feature in features:
        linear_output = sum(f * w for f, w in zip(feature, weights)) + bias
        out.append(linear_output)
	
    sigmoid_out = []
    for o in out:
        sigmoid_out.append(1 / (1 + math.exp(-o)))

    n = len(labels)
    s = 0
    for i in range(0, n):
        s += (sigmoid_out[i] - labels[i]) ** 2

	return (sigmoid_out, s/n)