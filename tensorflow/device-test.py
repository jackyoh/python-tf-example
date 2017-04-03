import tensorflow as tf

a = tf.constant([1.0,2.0,3.0,4.0], shape=[2,2],name='a')
b = tf.constant([1.0,2.0,3.0,4.0], shape=[2,2],name='b')
c = tf.matmul(a,b)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
