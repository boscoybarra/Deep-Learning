# Solution is available in the other "solution.py" tab
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session

# Cross entropy function
cross_entropy = - tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

with tf.Session() as session:
        output = session.run(cross_entropy,feed_dict={softmax: softmax_data, one_hot: one_hot_data})
        print(output)