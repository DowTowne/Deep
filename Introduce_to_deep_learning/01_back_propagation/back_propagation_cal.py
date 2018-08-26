#coding:utf-8

#当前脚本是为了记录推导反向传播的相关值而编写的

import math

#定义sigmoid激活函数
def activate(net):
    return 1/(1+math.exp(-net))
#定义更新权重的函数
def update_weight(w,rate,round):
    return w - rate*round
#输入
i1 = 0.05
i2 = 0.10
#输出
o1 = 0.01
o2 = 0.99

#权重
w1 = 0.15
w2 = 0.20
w3 = 0.25
w4 = 0.30

w5 = 0.40
w6 = 0.45
w7 = 0.50
w8 = 0.55

#偏置
b1 = 0.35
b2 = 0.60

#隐藏层
net_h1 = w1*i1 + w2*i2 + b1*1
net_h2 = w3*i1 + w4*i2 + b1*1
print(net_h1)
print(net_h2)
out_h1 = activate(net_h1)
out_h2 = activate(net_h2)
print('out_h1：' + str(out_h1))
print('out_h2：' + str(out_h2))

#输出层
net_o1 = w5*out_h1 + w6*out_h2 + b2*1
net_o2 = w7*out_h1 + w8*out_h2 + b2*1
print('net_o1：' + str(net_o1))
print('net_o2：' + str(net_o2))
out_o1 = activate(net_o1)
out_o2 = activate(net_o2)
print('out_o1：'+ str(out_o1))
print('out_o2：' + str(out_o2))

#总误差
E_total = (math.pow(o1-out_o1,2) + math.pow(o2-out_o2,2))/2
print('Total Error：' + str(E_total))

#E_total对w5的偏导数
round_E_total_w5 = -(o1-out_o1)*out_o1*(1-out_o1)*out_h1
round_E_total_w6 = -(o1-out_o1)*out_o1*(1-out_o1)*out_h2
round_E_total_w7 = -(o2-out_o2)*out_o2*(1-out_o2)*out_h1
round_E_total_w8 = -(o2-out_o2)*out_o2*(1-out_o2)*out_h2
print('round_E_total_w5: '+ str(round_E_total_w5))
print('round_E_total_w6: '+ str(round_E_total_w6))
print('round_E_total_w7: '+ str(round_E_total_w7))
print('round_E_total_w8: '+ str(round_E_total_w8))

learning_rate = 0.5
w5_1 = w5 - learning_rate * round_E_total_w5
w6_1 = w6 - learning_rate * round_E_total_w6
w7_1 = w7 - learning_rate * round_E_total_w7
w8_1 = w8 - learning_rate * round_E_total_w8
print('new w5: ' + str(w5_1))
print('new w6: ' + str(w6_1))
print('new w7: ' + str(w7_1))
print('new w8: ' + str(w8_1))

round_E_total_w1 = (-(o1-out_o1)*out_o1*(1-out_o1)*w5 +(-1)*(o2-out_o2)*out_o2*(1-out_o2)*w7)*out_h1*(1-out_h1)*i1
round_E_total_w2 = (-(o1-out_o1)*out_o1*(1-out_o1)*w5 +(-1)*(o2-out_o2)*out_o2*(1-out_o2)*w7)*out_h1*(1-out_h1)*i2
round_E_total_w3 = (-(o1-out_o1)*out_o1*(1-out_o1)*w6 +(-1)*(o2-out_o2)*out_o2*(1-out_o2)*w8)*out_h2*(1-out_h2)*i1
round_E_total_w4 = (-(o1-out_o1)*out_o1*(1-out_o1)*w6 +(-1)*(o2-out_o2)*out_o2*(1-out_o2)*w8)*out_h2*(1-out_h2)*i2
print('round_E_total_w1：' + str(round_E_total_w1))
print('round_E_total_w2：' + str(round_E_total_w2))
print('round_E_total_w3：' + str(round_E_total_w3))
print('round_E_total_w4：' + str(round_E_total_w4))

w1_1 = w1 - learning_rate * round_E_total_w1
w2_1 = w2 - learning_rate * round_E_total_w2
w3_1 = w3 - learning_rate * round_E_total_w3
w4_1 = w4 - learning_rate * round_E_total_w4
print('new w1：' + str(w1_1))
print('new w2：' + str(w2_1))
print('new w3：' + str(w3_1))
print('new w4：' + str(w4_1))

#经过第一次反向传播重新计算一下总误差
net_h1 = w1_1*i1 + w2_1*i2 + b1*1
net_h2 = w3_1*i1 + w4_1*i2 + b1*1
out_h1 = activate(net_h1)
out_h2 = activate(net_h2)
net_o1 = w5_1*out_h1 + w6_1*out_h2 + b2*1
net_o2 = w7_1*out_h1 + w8_1*out_h2 + b2*1
out_o1 = activate(net_o1)
out_o2 = activate(net_o2)
#总误差
E_total = (math.pow(o1-out_o1,2) + math.pow(o2-out_o2,2))/2
print('Total Error Update：' + str(E_total))
