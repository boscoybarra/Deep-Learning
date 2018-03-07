import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Create TensorFlow object called tensor

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

def run(param):
    output = None

    with tf.Session() as sess:
        output = sess.run(param, feed_dict={x: 'Test String', y: 123, z: 45.67})
        print(output)

    return output


def run_2():
    output = None
    x = tf.placeholder(tf.int32)

    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x, feed_dict={x: 123})
        print(output)

    return output

run(z)
