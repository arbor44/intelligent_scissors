import numpy as np


def get_gradient_direction(p, q, Gx, Gy):
    """
    p, q: pixels coords
    Gx, Gy: normalized grads
    """
    Dp = np.array([Gy[p[0], p[1]], -Gx[p[0], p[1]]])
    Dq = np.array([Gy[q[0], q[1]], -Gx[q[0], q[1]]])

    p, q = np.array(p), np.array(q)
    norm = 1 / np.sqrt(np.sum((p - q) ** 2))
    L = norm * (p - q) if np.dot(Dp, q - p) < 0 else norm * (q - p)

    return (2 / 3) * np.pi * (np.arccos(np.dot(Dp, L)) + np.arccos(np.dot(L, Dq)))


def get_local_cost(q, p, **precomp):
    return 0.43 * precomp['lapl_zc'][q[0], q[1]] + 0.43 * get_gradient_direction(p, q, *precomp['grads']) + 0.14 * \
           precomp['grad_magn'][q[0], q[1]]
