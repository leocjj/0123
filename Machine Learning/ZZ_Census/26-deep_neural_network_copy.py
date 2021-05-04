#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from pickle import load, dump
from os.path import isfile
from time import ctime


def sigmoid(x):
    """
    https://stackoverflow.com/questions/3985619/
    how-to-calculate-a-logistic-sigmoid-function-in-python
    Y = 1. / (1. + np.exp(-x))
    :param x: int or array. Use math.ext instead of np.exp for integers.
    :return: sigmoid function of x
    """
    return np.exp(-np.logaddexp(0., -x))

def tanh(x):
    """
    :param x: int or array. Use math.ext instead of np.exp for integers.
    :return: tanh function of x
    """
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


class DeepNeuralNetwork:
    """ Class that defines a deep neural network performing binary classification: """

    def __init__(self, nx, layers):
        """
        Defines a neural network performing binary classification
        :param nx: number of input features to the neuron
        :param layers: is the number of nodes found in the hidden layer
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(layers, list) or not list:
            raise TypeError('layers must be a list of positive integers')
        if not np.issubdtype(np.array(layers).dtype, np.integer) or\
                not all(np.array(layers) >= 1):
            raise TypeError('layers must be a list of positive integers')

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {'W1':
                          np.random.randn(layers[0], nx) * np.sqrt(2 / nx),
                          'b1': np.zeros((layers[0], 1))
                          }

        for i in range(1, self.__L):
            self.__weights["W" + str(i + 1)] = np.random.randn(layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])
            self.__weights["b" + str(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """  getter method """
        return self.__L

    @property
    def cache(self):
        """  getter method """
        return self.__cache

    @property
    def weights(self):
        """  getter method """
        return self.__weights

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron, using a sigmoid activation function.
        :param X: is a numpy.ndarray with shape (nx, m) that contains the input
            nx is the number of input features to the neuron,
            m is the number of examples.
        :return: the output of the neural network and the cache, respectively.
        """

        self.__cache["A0"] = X
        for i in range(1, self.L + 1):
            self.__cache["A" + str(i)] = sigmoid(
                np.matmul(self.weights["W" + str(i)], self.cache["A" + str(i - 1)]) + self.weights["b" + str(i)]
            )
        return self.cache["A" + str(self.L)], self.cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        https://datascience.stackexchange.com/questions/22470/
        python-implementation-of-cost-function-in-logistic-regression-why-dot-multiplic
        :param Y: is a numpy.ndarray with shape (1, m) that contains the
            correct labels for the input data
        :param A: is a numpy.ndarray with shape (1, m) containing the activated
            output of the neuron for each example
        :return: return -1 / Y.shape[1] * np.sum( np.multiply(np.log(A), Y) +
            np.multiply(np.log(1.0000001 - A), (1 - Y)))
        """
        return -1 / Y.shape[1] * np.sum(np.multiply(np.log(A), Y) + np.multiply(np.log(1.0000001 - A), (1 - Y))
        )

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions
        :param X: is a numpy.ndarray with shape (nx, m) that contains the input
            nx is the number of input features to the neuron,
            m is the number of examples.
        :param Y: is a numpy.ndarray with shape (1, m) that contains the
            correct labels for the input data
        :return: tuple with the neuron’s prediction and the cost of the network
            Prediction is numpy.ndarray with shape (1, m) containing the
            predicted labels for each example and the label values should be 1
            if the output of the network is >= 0.5 and 0 otherwise
        """
        self.forward_prop(X)
        return np.heaviside(
            self.cache["A" + str(self.L)] - 0.5, 1
        ).astype(int), self.cost(Y, self.cache["A" + str(self.L)])

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron.
        Updates the private attributes __W1, __b1, __W2, and __b2
        :param Y: is a numpy.ndarray with shape (1, m) that contains the
            correct labels for the input data.
        :param cache: is a dictionary containing all the intermediary values
            of the network.
        :param alpha: is the learning rate
        :return: Nothing.
        """

        m = Y.shape[1]
        dZ = cache['A' + str(self.__L)] - Y
        m1 = (1 / m)
        for i in range(self.__L, 0, -1):
            dW = m1 * np.matmul(cache['A' + str(i - 1)], dZ.T)
            db = m1 * np.sum(dZ, axis=1, keepdims=True)
            dZ = np.matmul(self.__weights['W' + str(i)].T, dZ) *\
                (cache['A' + str(i - 1)] * (1 - cache['A' + str(i - 1)]))

            self.__weights['W' + str(i)] -= (alpha * dW).T
            self.__weights['b' + str(i)] -= (alpha * db)

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """
        Trains the neuron.
        Updates the private attributes __weights and __cache
        :param X: is a numpy.ndarray with shape (nx, m) that contains the input
            nx is the number of input features to the neuron,
            m is the number of examples.
        :param Y: is a numpy.ndarray with shape (1, m) that contains the
            correct labels for the input data
        :param iterations: is the number of iterations to train over
        :param alpha: is the learning rate
        :param verbose: is a boolean, print information about the training.
        :param graph: is a boolean that defines whether or not to graph
            information about the training once the training has completed.
        :param step: verbose and graph will be printed every step iterations.
        :return: the evaluation of the training data after iterations of
            training have occurred
        """
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 1:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if not (1 < iterations <= iterations):
                raise ValueError('step must be positive and <= iterations')


        costs = []
        steps = np.arange(0, iterations + step, step)
        for i in range(iterations + 1):
            self.forward_prop(X)
            if verbose and i % step == 0:
                cost = self.cost(Y, self.cache["A" + str(self.L)])
                print("{} Cost after {} iterations: {}".format(ctime(), i, cost))
                costs.append(cost)
            self.gradient_descent(Y, self.cache, alpha)

        if graph:
            plt.plot(steps, costs)
            plt.ylim(0, 0.6)
            plt.title("Training Cost")
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.show()
        return self.evaluate(X, Y)

    def save(self, filename):
        """
        Saves the instance object to a file in pickle format
        :param filename: is the file to which the object should be saved
        :return: None
        """
        if filename == '' or not filename:
            return None
        if not filename.endswith('.pkl'):
            filename += '.pkl'

        with open(filename, 'wb') as f:
            dump(self, f)

    @staticmethod
    def load(filename):
        """
        Loads a pickled DeepNeuralNetwork object.
        :param filename: is the file from which the object should be loaded
        :return: the loaded object, or None if filename doesn’t exist
        """
        if filename == '' or not filename:
            return None
        if not isfile(filename):
            return None

        with open(filename, 'rb') as f:
            a = load(f)
        return a