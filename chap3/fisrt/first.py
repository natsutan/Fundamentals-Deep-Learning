import tensorflow as tf
deep_learning = tf.constant('Deep Leaning')
session = tf.Session()
ret = session.run(deep_learning)
print(ret)

a = tf.constant(2)
b = tf.constant(3)
multiply = tf.mul(a, b)
ret = session.run(multiply)
print(ret)



