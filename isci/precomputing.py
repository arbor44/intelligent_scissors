import numpy as np
from skimage.filters import laplace, sobel_h, sobel_v


def get_lapl_crossing(image):
    return np.abs(laplace(image)) > 0.01


def get_grads(image):
    return sobel_h(image), sobel_v(image)


def get_normalized_grads(Gx, Gy):
    """
    Gx, Gy: non-normalized grads
    """
    G = np.sqrt(Gx ** 2 + Gy ** 2)
    inv_G = np.zeros_like(G)
    inv_G[G > 0] = 1 / G[G > 0]

    return Gx * inv_G, Gy * inv_G


def get_grad_magn(Gx, Gy):
    """
    Gx, Gy: non-normalized grads
    """
    G = np.sqrt(Gx ** 2 + Gy ** 2)
    G = G - np.min(G)
    return 1 - G / np.max(G)
