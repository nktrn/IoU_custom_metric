import numpy as np
from typing import Optional
from geometry.elements import Line, Point


def is_collinear(line1: Line, line2: Line) -> bool:
    val = line1.x_diff() * line2.y_diff() - line1.y_diff() * line2.x_diff()
    return np.round(val, 3) == 0


def intersection(line1: Line, line2: Line) -> Optional[Point]:
    if is_collinear(line1, line2):
        return None

    x = ((line1.start.x * line1.end.y - line1.start.y * line1.end.x) * line2.x_diff() -
         line1.x_diff() * (line2.start.x * line2.end.y - line2.start.y * line2.end.x)) / \
        (line1.x_diff() * line2.y_diff() - line1.y_diff() * line2.x_diff())

    y = ((line1.start.x * line1.end.y - line1.start.y * line1.end.x) * line2.y_diff() -
         line1.y_diff() * (line2.start.x * line2.end.y - line2.start.y * line2.end.x)) / \
        (line1.x_diff() * line2.y_diff() - line1.y_diff() * line2.x_diff())

    point_intersection = Point(x, y)

    if (not line1.contains_point(point_intersection)) or (not line2.contains_point(point_intersection)):
        return None

    return Point(x, y)
