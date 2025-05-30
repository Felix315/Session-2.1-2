import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.

        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the point for printing.

        :return: A string in the format 'point(x, y)'.
        """
        return f"point({self.x}, {self.y})"

    def __repr__(self):
        """
        Return the official string representation of the point.

        :return: Same as __str__ output.
        """
        return self.__str__() # use the same way of printing as str

    def distance_orig(self):
        """
        Calculate the distance from the origin (0,0) to this point.

        :return: The Euclidean distance from the origin.
        """
        return (self.x**2 + self.y**2)**0.5 # square root of the sum of x and y squared

    def __gt__(self, other):
        """
        Compare two points based on their distance from the origin.

        :param other: Another Point object.
        :return: True if this point is further from the origin than the other.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Check if two points are at the same distance from the origin.

        :param other: Another Point object.
        :return: True if both points are equally distant from the origin.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

# now we need to instantiate it!
p = Point(1,2) # p is an instance of 1 and 2
p2 = Point(2,3)
p4 = Point(4.4,-55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x=20
print(f"p.x={p.x} and p.y={p.y}")
print(p)
# create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10,10), # x value
                        random.randint(-10,10))) # y value
print("I got these 5 random points:")
print(points)
p=Point(3,4)
print(p.distance_orig()) # expect 5 answer
p2=Point(1,1)
print(f"I am comparing p > p2: {p > p2}") # I expect to have True
print("the sorted list of points is:")
points.sort()
print(points)
