#coding:utf-8

import math
import random
from Neuron import *

class NeuronLayer:
    def __init__(self,num_neurons, bias,learning_rate):
         self.learning_rate = learning_rate
         #同一层的神经元共享一个截距项b
         self.bias = bias if bias else random.random()
         self.neurons = []
         for i in range(num_neurons):
             self.neurons.append(Neuron(self.bias,learning_rate))

    #检查这一层神经元的数量、权重、截距等基本信息
    def inspect(self):
        print('Neurons:', len(self.neurons))
        for n in range(len(self.neuron)):
            print('Neuron', n)
            for w in range(len(self.neurons[n].weights)):
                print('  Weight:', self.neurons[n].weights[w])
                print(' Bias:', self.bias)

    #前向传播
    def feed_forward(self,inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.calculate_output(inputs))
        return outputs

    # 获取输出
    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.output)
        return  outputs


