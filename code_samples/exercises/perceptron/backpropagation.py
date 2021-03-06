import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

def sigmoid_prime(x):
    """
    # Derivative of the sigmoid function
    """
    return sigmoid(x) * (1 - sigmoid(x))

def prime(x):
    """
    # Derivative of the sigmoid function
    """
    return x * (1 - x)

x = np.array([0.5, 0.1, -0.2])
target = 0.6
learnrate = 0.5

weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])

weights_hidden_output = np.array([0.1, -0.3])

## Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_in)
print("output", output)

print(x.shape)

print(hidden_layer_input.shape)
print(output_layer_in.shape)


## Backwards pass
## TODO: Calculate output error
error = (target - output)

# TODO: Calculate error term for output layer
output_error_term = np.dot(error, prime(output))
print("Output error term:", output_error_term)

# TODO: Calculate error term for hidden layer
hidden_error_term = np.dot(weights_hidden_output,output_error_term) * prime(hidden_layer_output)
print(hidden_error_term)

# TODO: Calculate change in weights for hidden layer to output layer
delta_w_h_o = learnrate * output_error_term * hidden_layer_output

print(x.shape)
print(hidden_error_term.shape)

# TODO: Calculate change in weights for input layer to hidden layer
delta_w_i_h = learnrate * hidden_error_term * x[:, None]

print('Change in weights for hidden layer to output layer:')
print(delta_w_h_o)
print('Change in weights for input layer to hidden layer:')
print(delta_w_i_h)
