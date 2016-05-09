import tensorflow as tf


def inference(x):
	tf.constant_initializer(value=0)
	W = tf.get_variable("W", [784,10], initializer=init)
	b = tf.get_variable("b", [10], initiralizer=init)
	output = tf.nn.softmax(tf.matmul(x, W)+b)
	return output
	  
