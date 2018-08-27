#coding:utf-8
import math

# z 是权重计算值
# a 是激活计算之后的值

"""定义一个简单的神经元"""
class Neuron:
    def __init__(self,bias,learning_rate):
        self.learning_rate = learning_rate
        self.bias = bias
        self.weights = []


    #激活函数,net为网络计算值
    def activation(self,net):
        return 1 / (1 + math.exp(-net))

    #计算每一个神经元的误差（均方差）
    def calculate_error(self,target_out):
        return self.learning_rate  * (target_out - self.output)**2

    #根据权重计算网络值z
    def calculate_net(self):
        total = 0
        for i in range(len(self.inputs)):
            total += self.inputs[i] * self.weights[i]
        return total + self.bias

    #计算输出
    def calculate_output(self,inputs):
        self.inputs = inputs
        self.output = self.activation(self.calculate_net())
        return self.output

    #计算网络计算值z对输入的偏导数
    def calculate_round_net_to_input(self):
        return  self.output * (1 - self.output)

    #计算误差对网络值的偏导
    def calculate_round_error_to_net(self,target_output):
        return  self.calculate_round_error_to_out(target_output) * self.calculate_round_net_to_input();

    #计算误差对输出值的偏导
    def calculate_round_error_to_out(self,target_out):
        return -(target_out - self.output)

    #Y计算网络值对输入的偏导
    def calculate_round_output_to_input(self):
        return self.output * (1-self.output)

    #计算网络值对权重的偏导
    def calculate_round_net_to_weight(self,index):
        return self.inputs[index]
