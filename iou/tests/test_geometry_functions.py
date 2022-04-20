from iou.geometry import Point, Line, euclidean_distance, is_collinear, intersection


def test_euclidean_distance():
    p1 = Point(0, 0)
    p2 = Point(2, 2)
    assert 2 * 2 ** 0.5 == euclidean_distance(p1, p2)


def test_is_collinear__lines_not_collinear():
    line1 = Line(Point(0, 0), Point(100, 0))
    line2 = Line(Point(50, -50), Point(50, 50))
    assert not is_collinear(line1, line2)


def test_is_collinear__lines_collinear():
    line1 = Line(Point(0, 0), Point(100, 0))
    line2 = Line(Point(50, 50), Point(100, 50))
    assert is_collinear(line1, line2)


def test_intersection():
    line1 = Line(Point(0, 0), Point(100, 0))
    line2 = Line(Point(50, -50), Point(50, 50))
    point = Point(50, 0)
    assert intersection(line1, line2) == point


def test_intersection__lines_have_not_got_intersection():
    line1 = Line(Point(0, 0), Point(100, 0))
    line2 = Line(Point(50, 50), Point(50, 100))
    assert intersection(line1, line2) == None
