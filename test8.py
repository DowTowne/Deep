import tensorflow as tf
import numpy as np

# 构造满足一元二次方程的函数
# 为了使点更加密一些，我们构建了300个点，分布在-1到1区间，直接采用np生成等差数列的方法，
# 并将结果为300个点的一维数组，转换为300*1的二维数组
x_data = np.linspace(-1,1,300)[:,np.newaxis] 

# 加入一些噪声点，使它与x_dat的维度一致，并且拟合为均值为0、方差为0.05的正太分布
noise = np.random.normal(0,0.05,x_data.shape)

# y = x^2 - 0.5 + 噪声
y_data = np.square(x_data) - 0.5 + noise

# 接下来定义x和y的点位符来作为将要输入神经网络的变量
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

def add_layer(inputs, in_size, out_size, activation_function=None):
    # 构建权重:in_size*out_size大小的矩阵
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    # 构建偏置：1*out_size的矩阵
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    # 矩阵相乘
    wx_plus_b = tf.matmul(inputs, weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs# 得到输出数据

# 构建隐藏层，假设隐藏层有10个神经元
h1 = add_layer(xs, 1, 20, activation_function=tf.nn.relu)
# 构建输出层，假设输出层和输入层一样，有1个神经元
prediction = add_layer(h1, 20, 1, activation_function=None)

# 接下来需要构建损失函数：计算输出层的预测值和真实值间的误差，对二者差的平方求和
# 再取平均，得到损失函数。运用梯度下降法，以0.1的效率最小化损失：
# 计算预测值和真实值间的误差
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
	reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

init = tf.global_variables_initializer()# 初始化所有变量
sess = tf.Session()
sess.run(init)

for i in range(10000):# 训练1000次
    sess.run(train_step,feed_dict={xs: x_data, ys: y_data})
    #if i % 50 == 0:# 每50次打印出一次损失值
    print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))





