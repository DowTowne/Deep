import tensorflow as tf

weights = tf.Variable(tf.random_normal([1, 20]))
# 添加用于初始化变量的节点
init = tf.global_variables_initializer()

# 然后，在加载模型的时候
with tf.Session() as sess:
    # 运行初始化操作
    sess.run(init)
    print(sess.run(weights))
