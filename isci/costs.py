import math


def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]


def get_gradient_direction(p, q, Gx, Gy):
    """
    p, q: pixels coords
    Gx, Gy: normalized grads
    """
    Dp = (Gy[p[0], p[1]], -Gx[p[0], p[1]])
    Dq = (Gy[q[0], q[1]], -Gx[q[0], q[1]])
    v = (q[0] - p[0], q[1] - p[1])

    if dot(Dp, v) < 0:
        v = (-v[0], -v[1])

    inv_norm = 1 / (v[0] ** 2 + v[1] ** 2) ** (1/2)
    L = (inv_norm * v[0], inv_norm * v[1])

    return (2 / 3) * math.pi * (math.acos(dot(Dp, L)) + math.acos(dot(L, Dq)))


def get_local_cost(q, p, **precomp):
    return 0.43 * precomp['lapl_zc'][q[0], q[1]] + 0.43 * get_gradient_direction(p, q, *precomp['grads']) + 0.14 * \
           precomp['grad_magn'][q[0], q[1]]
