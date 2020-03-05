def extract_seed(curve):
    return 0


def get_local_cost(q, p):
    return 0


def get_neigbours(point):
    return []


def path_search(curve):
    """

    :param curve: curve to connect with point
    :param point: new point
    :return: new curve
    """
    seed_point = extract_seed(curve)
    new_curve = {}
    active_pixels, expanded = {seed_point: 0}, []
    while len(active_pixels) > 0:
        min_pxl, min_cost = min(active_pixels.items(), key=lambda x: x[1])
        del active_pixels[min_pxl]

        if min_pxl not in expanded:
            expanded.append(min_pxl)

        for n in get_neigbours(min_pxl):
            if n in expanded:
                pass
            else:
                cost = min_cost + get_local_cost(min_pxl, n)
                if n in active_pixels.keys():
                    if cost < active_pixels.get(n):
                        del active_pixels[n]
                else:
                    active_pixels[n] = cost
                    new_curve[n] = min_pxl

    return new_curve

