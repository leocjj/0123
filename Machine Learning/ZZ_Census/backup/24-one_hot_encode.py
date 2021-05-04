#!/usr/bin/env python3
""" 0x01. Classification """
import numpy as np


def one_hot_encode(Y, classes):
    """
    Function that converts a numeric label vector into a one-hot matrix.
    :param Y: is a np.ndarray with shape (m,) containing numeric class labels.
    :param classes: is the maximum number of classes found in Y
    :return: a one-hot encoding of Y with shape (classes, m) or None on failure
    """

    if not isinstance(classes, int) or classes < 1:
        return None

    if not isinstance(Y, np.ndarray)\
            or not Y.ndim == 1\
            or not np.issubdtype(Y.dtype, np.integer)\
            or not np.all(0 <= Y)\
            or not np.all(Y < classes):
        return None

    A = np.zeros((classes, Y.shape[0]))
    for i in range(Y.shape[0]):
        A[Y[i]][i] = 1
    return A
