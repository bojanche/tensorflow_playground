#import tensorflow as tf
import tensorflow.compat.v1 as tf
import numpy as np

tf.disable_v2_behavior()


sess = tf.Session()
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))
