# Define Objective function
# Take gradients of the function till minimum is zero

import numpy as np
import argparse


class SGD:
    def __init__(self, lr=0.01, max_iter=1000, batch_size=32, tol=1e-3):
        self.learning_rate = lr
        self.max_iteration = max_iter
        self.batch_size = batch_size
        self.tolerance = tol
        self.theta = None

    def fit(self, X, y):
        n, d = X.shape
        self.theta = np.random.randn(d)
        for i in range(self.max_iteration):
            if i % 100 == 0:
                print("iteration number: ", i)
                indices = np.random.permutation(n)
                X = X[indices]
                y = y[indices]

                for i in range(0, n, self.batch_size):
                    X_batch = X[i:i + self.batch_size]
                    y_batch = y[i:i + self.batch_size]
                    grad = self.gradient(X_batch, y_batch)
                    self.theta -= self.learning_rate * grad

                if np.linalg.norm(grad) < self.tolerance:
                    break

    def gradient(self, X, y):
        n = len(y)
        y_pred = np.dot(X, self.theta)
        error = y_pred - y
        grad = np.dot(X.T, error) / n
        return grad

    def predict(self, X):
        y_pred = np.dot(X, self.theta)
        return y_pred


parser = argparse.ArgumentParser(description="Stochastic Gradient Descend Example")
parser.add_argument("--lr", type=float, required=False, default=0.01)
parser.add_argument("--max_iter", type=int, required=False, default=1000)
parser.add_argument("--batch_size", type=int, required=False, default=32)
parser.add_argument("--tol", type=float, required=False, default=1e-3)
args = parser.parse_args()
print(f"Arguments: {args}")

lr = args.lr
max_iter = args.max_iter
batch_size = args.batch_size
tolerance = args.tol

X = np.random.randn(10, 5)
y = np.dot(X, np.array([1, 2, 3, 4, 5])) + np.random.randn(10) * 0.1

model = SGD(lr=lr, max_iter=max_iter, batch_size=batch_size, tol=tolerance)
model.fit(X, y)
# Predict using predict method from model
y_pred = model.predict(X)


