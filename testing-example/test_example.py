import numpy as np

from utils import array_api_compatible


def normalize(arr):
    mean = np.mean(arr)
    std = np.std(arr)
    normalized_arr = (arr - mean) / std

    return normalized_arr


def test_normalize():
    arr = np.array([1., 2., 3., 4., 5., 6.], dtype=np.float32)
    res = normalize(arr)

    assert abs(np.mean(res)) < 1e-16
    assert abs(np.std(res) - 1) < 1e16
