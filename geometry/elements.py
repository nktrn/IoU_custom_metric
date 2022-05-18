from typing import List
import numpy as np


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def get_theta(self, centroid: 'Point') -> float:
        y = self.y - centroid.y
        x = self.x - centroid.y
        theta = np.arctan2(y, x)
        theta = theta * 180 / np.pi
        if theta < 0:
            theta = 360 + theta
        return theta


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def euclidean_distance(self, p1: Point, p2: Point) -> float:
        return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def contains_point(self, p: Point) -> bool:
        dist1 = self.euclidean_distance(self.start, p)
        dist2 = self.euclidean_distance(p, self.end)
        line_dist = self.euclidean_distance(self.start, self.end)
        return np.allclose(line_dist, dist1 + dist2, 1e-5)

    def x_diff(self) -> float:
        return self.start.x - self.end.x

    def y_diff(self) -> float:
        return self.start.y - self.end.y

    def orientation_is_left(self, p: Point) -> bool:
        val = -(p.y - self.start.y) * self.x_diff() + (p.x - self.start.x) * self.y_diff()
        return val >= 0


class Polygon:
    def __init__(self, *vertexes: Point):
        self.centroid = self._centroid(vertexes)
        self.vertexes = self._order_points(vertexes)
        self.n = len(self.vertexes)
        self.area = self._area()

    def _centroid(self, vertexes) -> Point:
        centroid_x = np.mean([vertex.x for vertex in vertexes])
        centroid_y = np.mean([vertex.y for vertex in vertexes])
        return Point(centroid_x, centroid_y)

    def _order_points(self, vertexes) -> List[Point]:
        thetas = np.array([vertex.get_theta(self.centroid) for vertex in vertexes])
        thetas_inds = thetas.argsort()
        vertexes = np.array(vertexes)
        vertexes = vertexes[thetas_inds].tolist()

        return vertexes

    def _area(self) -> float:
        a1 = sum([self.vertexes[i].x * self.vertexes[(i + 1) % self.n].y
                  for i in range(self.n)])

        a2 = sum([self.vertexes[i].y * self.vertexes[(i + 1) % self.n].x
                  for i in range(self.n)])

        return np.abs(a1 - a2) / 2

    def get_edges(self) -> List[Line]:
        return [
            Line(self.vertexes[i], self.vertexes[(i + 1) % self.n])
            for i in range(self.n)
        ]

    def contains_point(self, point: Point) -> bool:
        edges = [
            edge.orientation_is_left(point)
            for edge in self.get_edges()
        ]
        return all(edges)
