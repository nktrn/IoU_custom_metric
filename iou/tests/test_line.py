from iou.geometry import Point, Line


def test_contains_point():
    line = Line(
        Point(0, 0),
        Point(100, 0)
    )
    point = Point(50, 0)
    assert line.contains_point(point)


def test_contains_point__point_not_in_line():
    line = Line(
        Point(0, 0),
        Point(100, 0)
    )
    point = Point(50, 50)
    assert line.contains_point(point) == False


def test_orientation_point_on_the_left():
    line = Line(
        Point(0, 100),
        Point(0, 0)
    )
    point = Point(50, 50)
    assert line.orientation_is_left(point)


def test_orientation_point_on_the_right():
    line = Line(
        Point(100, 100),
        Point(0, 0)
    )
    point = Point(0, 50)
    assert line.orientation_is_left(point) == False


def test_orientation_point_on_line():
    line = Line(
        Point(100, 100),
        Point(0, 0)
    )
    point = Point(50, 50)
    assert line.orientation_is_left(point)
