import math
import random
import unittest
import pytest
from polygon import (
    Point,
    Vector,
    ConvexPolygon
)


class PolygonTest(unittest.TestCase):

    #Point
    def test_point_x(self):
        self.assertEqual(Point(1.20, 0.0).x, 1.20)

    def test_point_y(self):
        self.assertEqual(Point(1.20, 2.0).y, 2.0)

    def test_point_not_float(self):
        with pytest.raises(TypeError, match='Expected a value type: float'):
            Point(1,0)

    #Vector
    def test_vector_start(self):
        start: Point = Point(1.0, 3.0)
        end: Point = Point(3.0, 1.0)

        self.assertEqual(Vector(start, end).start, start)

    def test_vector_end(self):
        start: Point = Point(1.0, 3.0)
        end: Point = Point(3.0, 1.0)

        self.assertEqual(Vector(start, end).end, end)

    def test_vector_not_point(self):
        with pytest.raises(TypeError, match='Expected a value type: Point'):
            Vector(3, 2)

    def test_vector_x(self):
        start: Point = Point(1.0, 3.0)
        end: Point = Point(3.0, 1.0)

        self.assertEqual(Vector(start, end).x, 2.0)

    def test_vector_y(self):
        start: Point = Point(1.0, 3.0)
        end: Point = Point(3.0, 1.0)

        self.assertEqual(Vector(start, end).y, -2.0)

    def test_vector_magnitude(self):
        start: Point = Point(1.0, 1.0)
        end: Point = Point(2.0, 2.0)

        self.assertEqual(Vector(start, end).magnitude(), math.sqrt(2))

    def test_vector_magnitude_zero(self):
        start: Point = Point(1.0, 2.0)
        end: Point = Point(1.0, 2.0)

        self.assertEqual(Vector(start, end).magnitude(), 0.0)

    def test_vector_angle_between_vectors225(self):
        center: Point = Point(0.0, 0.0)
        x1: Point = Point(1.0, 0.0)
        y1: Point = Point(-1.0, -1.0)

        vector1: Vector = Vector(center, x1)
        vector2: Vector = Vector(center, y1)

        self.assertEqual(Vector.angle_between_vectors(vector1, vector2), 3.9269908169872414)

    def test_vector_angle_between_vectors45(self):
        center: Point = Point(0.0, 0.0)
        x1: Point = Point(1.0, 0.0)
        y1: Point = Point(1.0, 1.0)

        vector1: Vector = Vector(center, x1)
        vector2: Vector = Vector(center, y1)

        self.assertEqual(Vector.angle_between_vectors(vector1, vector2), 0.7853981633974484)

    def test_vector_angle_between_vectors_not_vector(self):
        with pytest.raises(TypeError, match='Expected arguments type: Vector, Vector'):
            Vector.angle_between_vectors(1, 2)

    #ConvexPolygon
    def test_convex_polygon_points(self):
        points = [Point(6.0, 5.0), Point(-3.0, -4.0), Point(10.0, -4.0)]

        self.assertEqual(ConvexPolygon(points).points, points)

    def test_convex_polygon_sort_3points(self):
        points = [Point(6.0, 5.0), Point(-3.0, -4.0), Point(10.0, -4.0)]

        self.assertEqual(ConvexPolygon([points[1], points[2], points[0]]).points, points)

    def test_convex_polygon_sort_13points(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]

        self.assertEqual(ConvexPolygon([points[4], points[2], points[5], points[0], points[6], points[3], points[1]]).points, points)

    def test_convex_polygon_points_2points(self):
        points = [Point(6.0, 5.0), Point(-3.0, -4.0)]

        with pytest.raises(ValueError, match='Number of points must be 3 or greater!'):
            ConvexPolygon(points)

    def test_convex_polygon_points_not_list(self):
        with pytest.raises(TypeError, match='Expected a value type: List\\[Point\\]'):
            ConvexPolygon(1)

    def test_convex_polygon_points_not_list_of_points(self):
        with pytest.raises(TypeError, match = 'Expected type of an element of a list: Point'):
            ConvexPolygon(['r', 'a', 't', 'k', 'o'])

    def test_convex_polygon_is_convex1(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        polygon = ConvexPolygon(points)

        self.assertEqual(polygon._check_convex(), True)

    def test_convex_polygon_is_convex2(self):
        points = [Point(14.0, 7.0), Point(6.0, 14.0), Point(2.0, 10.0), Point(8.0, 3.0), Point(13.0, 10.0)]
        polygon = ConvexPolygon(points)

        self.assertEqual(polygon._check_convex(), True)

    def test_convex_polygon_not_convex1(self):
        points = [Point(9.0, 10.0), Point(6.0, 14.0), Point(2.0, 10.0), Point(8.0, 3.0), Point(13.0, 10.0)]

        with pytest.raises(ValueError, match = 'Polygon is not convex!'):
            ConvexPolygon(points)

    def test_convex_polygon_not_convex2(self):
        points = [Point(9.0, 10.0), Point(6.0, 14.0), Point(2.0, 10.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -7.0), Point(8.0, 3.0)]

        with pytest.raises(ValueError, match = 'Polygon is not convex!'):
            ConvexPolygon(points)

    def test_convex_polygon_contains1(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(-4.0, 5.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), True)

    def test_convex_polygon_contains2(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(3.0, 6.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), True)

    def test_convex_polygon_contains3(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(13.0, 10.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), True)

    def test_convex_polygon_contains_not1(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(13.0, -9.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), False)

    def test_convex_polygon_contains_not2(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(13.0, 6.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), False)

    def test_convex_polygon_contains_not3(self):
        points = [Point(13.0, 10.0), Point(6.0, 14.0), Point(-6.0, 15.0), Point(-14.0, 7.0), Point(-9.0, -5.0), Point(3.0, -11.0), Point(10.0, -4.0)]
        point_to_check = Point(-16.0, -4.0)

        self.assertEqual(ConvexPolygon(points).contains(point_to_check), False)









