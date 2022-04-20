from itertools import product

from iou.geometry import Polygon, intersection


def iou(true_polygon: Polygon, predict_polygon: Polygon) -> float:
    t_points = [
        vertex
        for vertex in true_polygon.vertexes
        if predict_polygon.contains_point(vertex)
    ]
    p_points = [
        vertex
        for vertex in predict_polygon.vertexes
        if true_polygon.contains_point(vertex)
    ]

    if len(t_points) == 0 and len(p_points) == 0:
        return 0

    i_points = [
        intersection(edges[0], edges[1])
        for edges in product(true_polygon.get_edges(), predict_polygon.get_edges())
        if intersection(edges[0], edges[1])
    ]

    points = t_points + p_points + i_points

    intersection_polygon = Polygon(*points)
    res = intersection_polygon.area / (predict_polygon.area + true_polygon.area - intersection_polygon.area)

    return res