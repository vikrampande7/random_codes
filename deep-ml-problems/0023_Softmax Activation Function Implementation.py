import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	exp_sum = 0
	for s in scores:
		exp_sum += math.exp(s)
	return [math.exp(p)/exp_sum for p in scores]