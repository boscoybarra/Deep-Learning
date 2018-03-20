import numpy as np

# Output (prediction) formula
# The feature is the relevance we want to give to that data set in order to add more or less importance to the non linear representation
def output_formula(features, weights, bias):
    w = weights
    x = features
    b = bias
    return sigmoid(np.dot(x, w) + b)
print("Combination of perceptrons")
print(output_formula([0.4, 0.6], [2, 6], -2))
print(output_formula([0.4, 0.6], [3, 5], -2.2))
print(output_formula([0.4, 0.6], [5, 4], -3))

# Error (log-loss) formula
def error_formula(y, output):
    return - y*np.log(output) - (1 - y) * np.log(1-output)

# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
    w = weights
    b = bias
    a = learnrate
    output = output_formula(x, w, b)
    d_error = -(y - output)
    weights -= a * d_error * x
    bias -= a * d_error
    return weights, bias

# Defining the sigmoid function for activations
def sigmoid(x):
    return 1/(1+np.exp(-x))
    # Can also be represented as:
    # return np.divide(1, (1 + np.exp(-x)))

print(sigmoid(2.4))
print(sigmoid(2))
print(sigmoid(-2.6))
