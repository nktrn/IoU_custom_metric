import pytest

from iou.geometry import Point, Polygon


@pytest.fixture()
def polygon():
    point1 = Point(0, 0)
    point2 = Point(0, 100)
    point3 = Point(100, 100)
    point4 = Point(100, 0)
    polygon = Polygon(point1, point2, point3, point4)
    return polygon


def test__centroid(polygon):
    centroid = Point(50.0, 50.0)
    assert centroid == polygon.centroid


def test__order_points(polygon):
    point1 = Point(0, 0)
    point2 = Point(0, 100)
    point3 = Point(100, 100)
    point4 = Point(100, 0)
    ordered_points = [point3, point2, point1, point4]

    assert all([ordered_points[i] == polygon.vertexes[i] for i in range(4)])


def test__area(polygon):
    assert 100 * 100 == polygon.area


def test_contains_point(polygon):
    point = Point(50, 50)
    assert polygon.contains_point(point)


def test_contains_point_point_not_in_polygon(polygon):
    point = Point(150, 100)
    assert not polygon.contains_point(point)
