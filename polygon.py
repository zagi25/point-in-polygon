from __future__ import annotations
import matplotlib.pyplot as plt
import math
from typing import List, Tuple

class Vector:
    '''
    A class to represent a vector.

    Properties:

        start: Point
            starting point of vector
        end: Point
            ending point of vector
        x: float
            vector x-component
        y: float
            vector y-component

    Staticmethods:

        angle_between_vectors(vector1, vector2):
            returns angle between two vectros in radians.
    '''
    def __init__(self, start: Point, end: Point) -> None:
        '''
        Constructs all the necessery properties for the vector object and calculates vectors x and y components

        Parameters:
            start: Point
                starting point of vector
            end: Point
                ending point of vector
        '''
        self.start = start
        self.end = end
        self.x = self.end.x - self.start.x
        self.y = self.end.y - self.start.y

    #Getters and Setters
    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value: Point):
        if isinstance(value, Point):
            self._start = value
        else:
            raise TypeError('Expected a value type: Point')

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value: Point):
        if isinstance(value, Point):
            self._end = value
        else:
            raise TypeError('Expected a value type: Point')

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        if isinstance(value, float):
            self._x = value
        else:
            raise TypeError('Expected a value type: float')

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        if isinstance(value, float):
            self._y = value
        else:
            raise TypeError('Expected a value type: float')


    def magnitude(self) -> float:
        '''
        '''

        return math.sqrt(self.x ** 2 + self.y ** 2)


    @staticmethod
    def angle_between_vectors(vector1: Vector, vector2: Vector) -> float:
        '''
        Returns the angle between two vectors in radians.

            Parameters:
                vector1: Vector
                vector2: Vector

            Returns:
                angle: float:
                    angle between two vectors in radians.
        '''
        if isinstance(vector1, Vector) and isinstance(vector2, Vector):
            #Vector magnitudes
            vector1_mag = vector1.magnitude()
            vector2_mag = vector2.magnitude()

            #Dot product
            dot_prod: float = vector1.x * vector2.x + vector1.y * vector2.y
            mag_prod: float = vector1_mag * vector2_mag

            #Angle is calculated by the formula: angle = arccos(dot product / magnitude product)
            try:
                angle: float = math.acos(dot_prod / mag_prod)
            except ZeroDivisionError:
                angle = 0.0

            #Cross prodcut of vectors. That product determines if our angle > 0 or angle < 0.
            angle_orientaion: float = vector1.x * vector2.y - vector1.y * vector2.x

            #If angle < 0 we substract angle from 2pi
            if angle_orientaion < 0:
                angle = 2 * math.pi - angle

            return angle
        else:
            raise TypeError('Expected arguments type: Vector, Vector')


class Point:
    '''
    A class to represent a point.

        Properties:

            x: float
                point x coordinate.
            y: float
                point y coordinate.
    '''
    def __init__(self, x: float, y: float) -> None:
        '''
        Constructs all the necessery properties for the point object.

            Parameters:
                x: float
                    point x coordinate.
                y: float
                    point y coordinate.
        '''
        self.x = x
        self.y = y

    #Getters and Setters
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        if isinstance(value, float):
            self._x = value
        else:
            raise TypeError('Expected a value type: float')

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        if isinstance(value, float):
            self._y = value
        else:
            raise TypeError('Expected a value type: float')


class ConvexPolygon:
    '''
    A class to represent a convex polygon.

        Properties:

            points: List[Point]
                list of points of polygon.

        Methods:

            contains(point: Point):
                returns if polygon contains point or not.

            draw(points: Point, contains: bool):
                plots polygon and provided point and writes does polygon contians point.
    '''
    def __init__(self, points: List[Point]) -> None:
        '''
        Constructs all the necessery properties for the convex polygon object, sorts points in counterclockwise order
        and checks if polygon is convex.

            Parameters:

                points: List[Point]
                    list of points of polygon.
        '''
        self.points = self._sort_points(points)
        self._check_convex()

    #Getters and Setters
    @property
    def points(self) -> List[Point]:
        return self._points

    @points.setter
    def points(self, value) -> None:
        if isinstance(value, list):
            if all(isinstance(element, Point) for element in value):
                if len(value) < 3:
                    raise ValueError('Number of points must be 3 or greater!')
                self._points = value
            else:
                raise TypeError('Expected type of an element of a list: Point')
        else:
            raise TypeError('Expected a value type: List[Point]')


    def _sort_points(self, points: List[Point]) -> List[Point]:
        '''
        Returns list of points sorted counterclockwise.

            Parameters:
                points: List[Point]
                    list of points of polygon.

            Returns:
                List[Point]
                    counterclockwise sorted list of points.
        '''
        if isinstance(points, list):
            if all(isinstance(element, Point) for element in points):
                sum_x: float = 0
                sum_y: float = 0

                #Sum of all x and all y coordinates
                for p in points:
                    sum_x += p.x
                    sum_y += p.y

                #Calculating mean of x and y coordinates to find center of polygon
                mean_x: float = sum_x / len(points)
                mean_y: float = sum_y / len(points)

                #Center of polygon
                center: Point = Point(mean_x, mean_y)
                #Point x + 1 away from center
                center_1: Point = Point(center.x + 1, center.y)

                #Vector form center to center_1
                center_vector: Vector = Vector(center, center_1)

                tmp_points: List[Tuple[float, Point]] = []

                #Calculating angle between center_vector and vector from center to point of polygon
                for p in points:
                    vector2: Vector = Vector(center, p)

                    angle = Vector.angle_between_vectors(center_vector, vector2)

                    #Storing tuple of angle and point
                    tmp_points.append((angle, p))

                #Sorting from smallest to largest angle
                tmp_points.sort()

                return [p[1] for p in tmp_points]
            else:
                raise TypeError('Expected type of an element of a list: Point')
        else:
            raise TypeError('Expected a value type: List[Point]')


    def _check_convex(self):
        '''
        Checks if polygon is convex.

            Returns:
                bool:
                    is polygon convex or not.
        '''
        for i in range(len(self.points)):
            #If last point take first and second point to form vectors
            if i == len(self.points) - 1:
                point1: Point = self.points[i]
                point2: Point = self.points[0]
                point3: Point = self.points[1]
            else:
                point1: Point = self.points[i]
                point2: Point = self.points[i + 1]
                #If second to last takse first point to form vectors
                point3: Point = self.points[0 if i == len(self.points) - 2 else i + 2]

            vector1: Vector = Vector(point1, point2)
            vector2: Vector = Vector(point2, point3)

            #Calculating cross product of vectors
            is_convex: float = vector1.x * vector2.y - vector1.y * vector2.x

            #Because we are moving counterclockwise every cross product needs to be counterclockwise
            #If not polygon is not convex raise ValueError
            if is_convex <= 0:
                raise ValueError('Polygon is not convex!')

        #If Exception was not raised return True
        return True


    def contains(self, point: Point) -> bool:
        '''
        Returns if polygon contains provieded point or not.

            Parameters:
                point: Point
                    point to check.

            Returns:
                bool:
                    is point in polygon.
        '''
        if isinstance(point, Point):
            for i in range(len(self.points)):
                #Construct vector from two points
                if i == len(self.points) - 1:
                    point2: Point = self.points[0]
                else:
                    point2: Point = self.points[i + 1]

                point1: Point = self.points[i]

                vector1: Vector = Vector(point1, point2)
                #Construct vector from point2 to provided point
                vector2: Vector = Vector(point2, point)

                #Coss product to check if point is on the 'left' or 'right' of vector
                position: float = vector1.x * vector2.y - vector1.y * vector2.x

                #Because we are moving counterclockwise point needs to be on the 'left' side of every vector
                #If point is not on the 'left' point is not in polygon
                if position < 0:
                    return False

            #If point is on the 'left' side of every vector point is in polygon
            return True
        else:
            raise TypeError('Expected an argument type: Point')


    def draw(self, point: Point, contains: bool) -> None:
        '''
        Draws polygon and provided point and writes if polygon contains point or not.

            Parameters:
                point: Point
                    point to draw.
                contains: bool
                    does polygon contains point.

        '''
        if isinstance(point, Point) and isinstance(contains, bool):
            if contains:
                text: str = f'Polygon contains point {point.x, point.y}'
            else:
                text: str = f'Polygon doesn\'t contains point {point.x, point.y}'

            #List of tuples containing x and y coordinates of point
            coord: List[Tuple[float, float]] = [(p.x, p.y) for p in self.points]

            #Repeat the first point to create a 'closed loop'
            coord.append(coord[0])

            #Create lists of x and y values
            x,y = zip(*coord)

            plt.figure()
            plt.rc('grid', linestyle="--")
            plt.scatter(x, y, color='darkorange', s = 70)
            plt.plot(x,y)

            #If polygon contains point color is green else red
            plt.scatter(point.x, point.y, color = 'green' if contains else 'red', s = 90)

            max_x: float = self.points[0].x
            for p in self.points:
                if p.x > max_x:
                    max_x = p.x

                #If x coordinate is max move it to left
                if p.x == max_x:
                    #Add coordinate values above point
                    plt.annotate((p.x, p.y), (p.x, p.y), (p.x - 0.4, p.y + 0.1))
                else:
                    plt.annotate((p.x, p.y), (p.x, p.y), (p.x + 0.1, p.y + 0.1))

            #Add coordinate values above point
            plt.annotate((point.x, point.y), (point.x, point.y), (point.x + 0.1, point.y + 0.1))

            plt.figtext(0.5, 0.04, text, horizontalalignment = 'center', fontsize = 15)
            plt.grid()
            plt.show()

        else:
            raise ValueError('Expected arguments type: Point, bool')
