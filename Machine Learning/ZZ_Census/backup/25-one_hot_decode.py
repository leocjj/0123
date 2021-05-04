#!/usr/bin/env python3
""" 0x01. Classification """
import numpy as np


def one_hot_decode(one_hot):
    """
    Function that converts a one-hot matrix into a vector of labels.
    :param one_hot: is a one-hot encoded numpy.ndarray with shape (classes, m)
        classes is the maximum number of classes
        m is the number of examples
    :return: a numpy.ndarray with shape (m, ) containing the numeric labels for
        each example, or None on failure
    """
    if not isinstance(one_hot, np.ndarray) \
            or not one_hot.ndim == 2 \
            or not one_hot.shape[0] > 0 \
            or not one_hot.shape[1] > 0 \
            or not np.all(0 <= one_hot)\
            or not np.all(one_hot <= 1):
        return None

    result = np.array([])
    for i in range(one_hot.shape[1]):
        temp = np.where(one_hot[:, i] == 1)
        if len(temp[0]) != 1:
            return None
        result = np.append(result, temp[0][0]).astype(int)

    return result
