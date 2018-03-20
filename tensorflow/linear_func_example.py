import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Linear Function
x = tf.Variable(5)
print(x)

# Initialization
# This tensor stores its state in the session, so you must initialize the state of the tensor manually.
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

# tf.truncated_normal()
# Choosing weights from a normal distribution prevents any one weight from overwhelming other weights. 
# tf.truncated_normal() function to generate random numbers from a normal distribution.
# Returns a tensor with random values from a normal distribution whose magnitude is no more than 2 standard deviations from the mean.

n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))


# tf.zeros()
# The tf.zeros() function returns a tensor with all zeros.
n_labels = 5
bias = tf.Variable(tf.zeros(n_labels))

print(x)
print(bias)
print(weights)