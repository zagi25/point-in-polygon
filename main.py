#!/usr/bin/env python3
import sys
from typing import Optional, List
from errors import DuplicatePoint
from polygon import Point, ConvexPolygon

def main() -> None:
    num_of_points: Optional[int] = None
    points: List[Point] = []

    #Input
    while True:
        try:
            if not num_of_points:
                #Number of points
                num_of_points = int(input('Enter a number of points of polygon: '))
            else:
                #If num_of_points < 3
                num_of_points = int(input('Enter a number larger than 2: '))

            if num_of_points < 3:
                continue

            print('Enter points coordinates:')

            i: int = 0
            last: bool = False

            while i < num_of_points + 1:
                #If last point collect point_to_check data else collecto point data
                if last:
                    print('\n  Point to check:')
                else:
                    print(f'  Point {i + 1}:')

                try:
                    tmp_x: float = float(input('    X: '))
                    tmp_y: float = float(input('    Y: '))
                    tmp_point: Point = Point(tmp_x, tmp_y)

                    if last:
                        global point_to_check
                        point_to_check = tmp_point
                    else:
                        for p in points:
                            #If point already exists throw an exception
                            if p.x == tmp_point.x and p.y == tmp_point.y:
                                raise DuplicatePoint

                        points.append(tmp_point)

                    if i == num_of_points - 1:
                        last = True

                    i += 1

                #If coordinates not number
                except ValueError:
                    print('Coordinate must be a number!')

                #If duplicate point
                except DuplicatePoint:
                    print('Point with this coordinates already exists!')

            break

        #If num_of_points is not a number go again
        except ValueError:
            num_of_points = None

        #Exit program on control-c
        except KeyboardInterrupt:
            sys.exit()


    polygon: ConvexPolygon = ConvexPolygon(points)
    contains = polygon.contains(point_to_check)

    if contains:
        print(f'Polygon contains point {point_to_check.x, point_to_check.y}')
    else:
        print(f'Polygon doesn\'t contains point {point_to_check.x, point_to_check.y}')

    polygon.draw(point_to_check, contains)


if __name__ == '__main__':
    main()
