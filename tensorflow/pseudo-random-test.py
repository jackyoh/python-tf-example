import tensorflow as tf
import matplotlib.pyplot as plt

uniform_with_seed = tf.random_uniform([1], seed = 1)
uniform_without_seed = tf.random_uniform([1])

with tf.Session() as first_session:
    print first_session.run(uniform_with_seed)
    print first_session.run(uniform_without_seed)

with tf.Session() as second_session:
    print second_session.run(uniform_with_seed)
    print second_session.run(uniform_without_seed)
