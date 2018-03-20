import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# keep_prob = tf.placeholder(tf.float32) # probability to keep units

# hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
# hidden_layer = tf.nn.relu(hidden_layer)
# hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

# logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1])


# The code above illustrates how to apply dropout to a neural network.

# The tf.nn.dropout() function takes in two parameters:

# hidden_layer: the tensor to which you would like to apply dropout
# keep_prob: the probability of keeping (i.e. not dropping) any given unit
# keep_prob allows you to adjust the number of units to drop. In order to compensate for dropped units, tf.nn.dropout() multiplies all units that are kept (i.e. not dropped) by 1/keep_prob.

# During training, a good starting value for keep_prob is 0.5.

# During testing, use a keep_prob value of 1.0 to keep all units and maximize the power of the model.


# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)

#     for epoch_i in range(epochs):
#         for batch_i in range(batches):
#             sess.run(optimizer, feed_dict={
#                 features: batch_features,
#                 labels: batch_labels,
#                 keep_prob: 0.5})

#     validation_accuracy = sess.run(accuracy, feed_dict={
#         features: test_features,
#         labels: test_labels,
#         keep_prob: 0.5})



hidden_layer_weights = [
    [0.1, 0.2, 0.4],
    [0.4, 0.6, 0.6],
    [0.5, 0.9, 0.1],
    [0.8, 0.2, 0.8]]
out_weights = [
    [0.1, 0.6],
    [0.2, 0.1],
    [0.7, 0.9]]

# Weights and biases
weights = [
    tf.Variable(hidden_layer_weights),
    tf.Variable(out_weights)]
biases = [
    tf.Variable(tf.zeros(3)),
    tf.Variable(tf.zeros(2))]


# Input
features = tf.Variable([[0.0, 2.0, 3.0, 4.0], [0.1, 0.2, 0.3, 0.4], [11.0, 12.0, 13.0, 14.0]])

# TODO: Create Model with Dropout

keep_prob = tf.placeholder(tf.float32) # probability to keep units

hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
hidden_layer = tf.nn.relu(hidden_layer)
hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1])

# TODO: Print logits from a session
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    output = sess.run(logits, feed_dict={keep_prob: 0.5})
    print(output)





