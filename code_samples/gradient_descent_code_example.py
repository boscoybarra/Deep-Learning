import numpy as np

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    """
    # Derivative of the sigmoid function
    """
    return sigmoid(x) * (1 - sigmoid(x))

# The learning rate, eta in the weight step equation
learnrate = 0.5

# Input data
x = np.array([1, 2, 3, 4])

# Target
y = np.array(0.5)

# Initial weights
# Input to output weights
w = np.array([0.5, -0.5, 0.3, 0.1])

### Calculating gradient descent step for each weight
### Note: Some steps have been consilated, so there are
###       fewer variable names than in the above sample code

# The node's linear combination of inputs and weights
# the linear combination performed by the node (h in f(h) and f'(h))
h = np.dot(w,x)

# Output of neural network
# The neural network output (y-hat)
nn_output = sigmoid(h)

# Error of neural network
# Output gradient (f'(h))
error = y - nn_output

# This requires the output gradient, which we haven't
# specifically added a variable for.
# error term (lowercase delta)
output_gradient = sigmoid_prime(h)
error_term = error * output_gradient

# Calculate change in weights (Delta)
# Gradient descent step
del_w = learnrate * error_term * x

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(del_w)
