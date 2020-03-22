import numpy as np
from .costs import get_local_cost
from itertools import product


def get_neighbours(point, shape):
    neighbours = []
    for i in product((0, 1, -1), repeat=2):
        if np.sum(np.abs(i)) > 0:
            neighbour = np.array(point) + np.array(i)
            if (not any((neighbour - shape) >= 0)) & (not any(neighbour < 0)):
                neighbours.append(tuple(neighbour))
                if any(neighbour < 0):
                    print(not any(neighbour < 0))
                    print(neighbour)
    return neighbours


def path_search(seed_point, shape, **precomp):
    pointers = {}
    active_pixels, expanded = {seed_point: 0}, []
    while len(active_pixels) > 0:
        min_pxl, min_cost = min(active_pixels.items(), key=lambda x: x[1])
        del active_pixels[min_pxl]

        if min_pxl not in expanded:
            expanded.append(min_pxl)

        for n in get_neighbours(min_pxl, shape):
            if n in expanded:
                pass
            else:
                cost = min_cost + get_local_cost(min_pxl, n, **precomp)
                if n in active_pixels.keys():
                    if cost < active_pixels.get(n):
                        del active_pixels[n]

                if n not in active_pixels.keys():
                    active_pixels[n] = cost
                    pointers[n] = min_pxl

    return pointers


def extract_path(pointers, destination):
    path = []
    while pointers.get(destination) is not None:
        destination = pointers.get(destination)
        path.append(destination)
    return path
