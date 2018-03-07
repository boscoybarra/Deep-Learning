import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# Addition
x = tf.add(5, 2)  # 7

# Subtraction and Multiplication
x = tf.subtract(10, 4) # 6
y = tf.multiply(2, 5)  # 10

# Converting types
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1


# TODO: Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x,y), tf.cast(tf.constant(1), tf.float64))

# TODO: Print z from a session

with tf.Session() as sess:
        output = sess.run(z)
        print(output)
