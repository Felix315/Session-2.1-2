from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    A subclass of ColorPoint with restricted color options,
    custom getters/setters, and additional utility methods.
    """

    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint with additional validation.

        :param x: The x-coordinate.
        :param y: The y-coordinate.
        :param color: The color of the point (must be in COLORS).
        :raises PointException: If the color is not in the allowed list.
        """
        if color not in self.COLORS:
            raise PointException("Invalid colour, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Getter for x-coordinate.
        :return: The x-coordinate of the point.
        """
        return self._x # getter method

    @x.setter
    def x(self, value):
        """
        Setter for x-coordinate.
        :param value: New value for the x-coordinate.
        """
        self._x = value # "setter" method

    @property
    def y(self):
        """
        Getter for y-coordinate.
        :return: The y-coordinate of the point.
        """
        return self._y

    @property
    def color(self):
        """
        Getter for the color of the point.
        :return: The color of the point.
        """
        return self._color

    @classmethod
    def add_colour(cls, color):
        """
        Add a new valid color to the list of acceptable COLORS.

        :param color: The color string to add.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create an AdvancedPoint instance from a coordinate tuple.

        :param coordinate: A tuple (x, y).
        :param color: The color to assign (default is "red").
        :return: An instance of AdvancedPoint.
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate the Euclidean distance between two points.

        :param p1: First point (must have x and y attributes).
        :param p2: Second point (must have x and y attributes).
        :return: The distance as a float.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculate distance from this point to another point.

        :param p: Another point with x and y attributes.
        :return: The distance as a float.
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

AdvancedPoint.add_colour("rojo")
p = AdvancedPoint(1,2,"rojo")
print(p.x)
print(p)
print(p.distance_orig())
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))
