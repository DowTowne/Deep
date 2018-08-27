#coding:utf-8

import math
import random
from Neuron import *
from NeuronLayer import *

#一个只有三层的神经网络，包含一个输入层，一个隐含层，一个输出层
class NeuralNetwork:

    # 构造函数，初始化 学习率，输入神经元的个数，隐藏神经元的个数，输出神经元的个数，隐藏层的权重序列，输出层的权重序列，隐藏层的偏置，输出层的偏置
    def __init__(self,learning_rate,num_inputs,num_hidden,num_outputs,hidden_layer_weights=None,output_layer_weights = None,hidden_layer_bias = None,output_layer_bias = None):
        self.learning_rate = learning_rate
        self.num_inputs = num_inputs
        self.hidden_layer = NeuronLayer(num_hidden, hidden_layer_bias,learning_rate)
        self.output_layer = NeuronLayer(num_outputs, output_layer_bias,learning_rate)

        self.init_weights_from_inputs_to_hidden_layer_neurons(hidden_layer_weights)
        self.init_weights_from_hidden_layer_neurons_to_output_layer_neurons(output_layer_weights)

    def init_weights_from_inputs_to_hidden_layer_neurons(self,hidden_layer_weights):
        weight_num = 0
        for h in range(len(self.hidden_layer.neurons)):
            for i in range(self.num_inputs):
                if not hidden_layer_weights:
                    self.hidden_layer.neurons[h].weights.append(random.random())
                else:
                    self.hidden_layer.neurons[h].weights.append(hidden_layer_weights[weight_num])
                weight_num += 1

    def init_weights_from_hidden_layer_neurons_to_output_layer_neurons(self, output_layer_weights):
        weight_num = 0
        for o in range(len(self.output_layer.neurons)):
            for h in range(len(self.hidden_layer.neurons)):
                if not output_layer_weights:
                    self.output_layer.neurons[o].weights.append(random.random())
                else:
                    self.output_layer.neurons[o].weights.append(output_layer_weights[weight_num])
                weight_num += 1

    def inspect(self):
        print('------')
        print('* Inputs:{}'.format(self.num_inputs))
        print('------')
        print('Hidden Layer')
        self.hidden_layer.inspect()
        print('------')
        print('* Output Layer')
        self.output_layer.inspect()
        print('------')

    def feed_forward(self,inputs):
        hidden_layer_outpus = self.hidden_layer.feed_forward(inputs)
        return  self.output_layer.feed_forward(hidden_layer_outpus)

    def train(self, training_inputs, training_outputs):
        self.feed_forward(training_inputs)
        # 1. 输出神经元的值
        round_errors_to_output_neuron_net = [0] * len(self.output_layer.neurons)
        for o in range(len(self.output_layer.neurons)):

            #∂E/∂zⱼ
            round_errors_to_output_neuron_net[o] = self.output_layer.neurons[o].calculate_round_error_to_net(training_outputs[o])

        # 2. 隐含层神经元的值
            round_errors_to_hidden_neuron_net = [0] * len(self.hidden_layer.neurons)
            print(round_errors_to_output_neuron_net)
            for h in range(len(self.hidden_layer.neurons)):

                # dE/dyⱼ = Σ ∂E/∂zⱼ * ∂z/∂yⱼ = Σ ∂E/∂zⱼ * wᵢⱼ
                d_error_to_hidden_neuron_output = 0
                for o in range(len(self.output_layer.neurons)):
                    d_error_to_hidden_neuron_output += round_errors_to_output_neuron_net[o] * self.output_layer.neurons[o].weights[h]

                # ∂E/∂zⱼ = dE/dyⱼ * ∂zⱼ/∂
                round_errors_to_hidden_neuron_net[h] = d_error_to_hidden_neuron_output * self.hidden_layer.neurons[h].calculate_round_net_to_input()

            # 3. 更新输出层权重系数
            for o in range(len(self.output_layer.neurons)):
                for w_ho in range(len(self.output_layer.neurons[o].weights)):
                    # ∂Eⱼ/∂wᵢⱼ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢⱼ
                    round_error_to_weight = round_errors_to_output_neuron_net[o] * self.output_layer.neurons[o].calculate_round_net_to_weight(w_ho)

                    # Δw = α * ∂Eⱼ/∂wᵢ
                    self.output_layer.neurons[o].weights[w_ho] -= self.learning_rate * round_error_to_weight

            # 4. 更新隐含层的权重系数
            for h in range(len(self.hidden_layer.neurons)):
                 for w_ih in range(len(self.hidden_layer.neurons[h].weights)):

                     # ∂Eⱼ/∂wᵢ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢ
                     round_error_to_weight = round_errors_to_hidden_neuron_net[h] * self.hidden_layer.neurons[h].calculate_round_net_to_weight(w_ih)

                     # Δw = α * ∂Eⱼ/∂wᵢ
                     self.hidden_layer.neurons[h].weights[w_ih] -= self.learning_rate * round_error_to_weight

    def calculate_total_error(self, training_sets):
         total_error = 0
         for t in range(len(training_sets)):
             training_inputs, training_outputs = training_sets[t]
             self.feed_forward(training_inputs)
             for o in range(len(training_outputs)):
                 total_error += self.output_layer.neurons[o].calculate_error(training_outputs[o])
         return total_error
