from point import Point
import random

class PointException(Exception):
    """
    Custom exception class for errors related to Point or ColorPoint usage.
    """
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint object, inheriting from Point.

        :param x: The x-coordinate (must be int or float).
        :param y: The y-coordinate (must be int or float).
        :param color: A string representing the color of the point.
        :raises PointException: If x or y is not a number.
        """
        # raise an exception if we try tro not have a number
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x, y) # this replaces the self.x and self.y
        self.color = color

    def __str__(self):
        """
        Return a string representation of the ColorPoint.

        :return: A string in the format '<color: x, y>'.
        """
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())
    print(p)
    # colors = ["red", "green", "blue", "yellow", "black", "magenta",
    #           "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # color_points = []
    # for i in range(10):
    #     color_points.append(
    #         ColourPoint(random.randint(-10, 10),
    #                     random.randint(-10, 10),
    #                     random.choice(colors)))
    #
    # print(color_points)
    # color_points.sort()
    # print(color_points)
