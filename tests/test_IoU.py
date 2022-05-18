import numpy as np

from geometry import Point, Polygon
from metric import iou


def test_IoU_same_polygons():
    true_polygon = Polygon(
        Point(0, 0),
        Point(0, 100),
        Point(100, 100),
        Point(100, 0)
    )
    predict_polygon = Polygon(
        Point(0, 0),
        Point(0, 100),
        Point(100, 100),
        Point(100, 0)
    )

    assert iou(true_polygon, predict_polygon) == 1


def test_IoU_no_intersections():
    true_polygon = Polygon(
        Point(1, 1),
        Point(2, 4),
        Point(4, 3),
        Point(3, 1)
    )
    predict_polygon = Polygon(
        Point(4.5, 4.5),
        Point(5.5, 4.5),
        Point(5.5, 3.5),
        Point(4.5, 3.5)
    )

    assert iou(true_polygon, predict_polygon) == 0


def test_IoU():
    true_polygon = Polygon(
        Point(1, 1),
        Point(2, 4),
        Point(4, 3),
        Point(3, 1)
    )
    predict_polygon = Polygon(
        Point(4, 5),
        Point(6, 4),
        Point(5, 1),
        Point(2, 2)
    )

    assert np.round(iou(true_polygon, predict_polygon), 2) == np.round(2.07 / (5.5 + 9 - 2.07), 2)
