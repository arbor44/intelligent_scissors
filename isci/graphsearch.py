from .costs import get_local_cost


def get_neighbour(point, shape):
    neighbours = []
    for i in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
        neighbour = (point[0] + i[0], point[1] + i[1])
        boundary_cross = (neighbour[0] >= shape[0] or neighbour[0] < 0) + (neighbour[1] >= shape[1] or neighbour[1] < 0)
        if boundary_cross == 0:
            neighbours.append(neighbour)
    return neighbours


def path_search(seed_point, shape, **precomp):
    pointers = {}
    active_pixels, expanded = {seed_point: 0}, set()
    length = 1
    while length > 0:
        min_pxl, min_cost = min(active_pixels.items(), key=lambda x: x[1])
        del active_pixels[min_pxl]
        length -= 1

        if min_pxl not in expanded:
            expanded.add(min_pxl)

        for n in get_neighbour(min_pxl, shape):
            if n in expanded:
                pass
            else:
                cost = min_cost + get_local_cost(min_pxl, n, **precomp)
                if active_pixels.get(n) is not None:
                    if cost < active_pixels.get(n):
                        del active_pixels[n]
                        length -= 1

                if active_pixels.get(n) is None:
                    active_pixels[n] = cost
                    length += 1
                    pointers[n] = min_pxl

    return pointers


def extract_path(pointers, destination):
    path = []
    while pointers.get(destination) is not None:
        destination = pointers.get(destination)
        path.append(destination)
    return path
