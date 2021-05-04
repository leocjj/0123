#!/usr/bin/env python3

import numpy as np

Deep = __import__('26-deep_neural_network').DeepNeuralNetwork
one_hot_encode = __import__('24-one_hot_encode').one_hot_encode
one_hot_decode = __import__('25-one_hot_decode').one_hot_decode

lib_train = np.load('../data/Binary_Train.npz')
X_train_3D, Y_train = lib_train['X'], lib_train['Y']
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1)).T

np.random.seed(0)
deep = Deep(X_train.shape[0], [3, 1])
A, cost = deep.train(X_train, Y_train, iterations=10, graph=False)
deep.save('26-output')
del deep

saved = Deep.load('26-output.pkl')
A_saved, cost_saved = saved.evaluate(X_train, Y_train)

print(np.array_equal(A, A_saved) and cost == cost_saved)
