class Point:
    def __init__(self, x, y):
        """
        Initialze a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"point({self.x}, {self.y})"

# now we need to instantiate it!
p = Point(1,2) # p is an instance of 1 and 2
p2 = Point(2,3)
p4 = Point(4.4,-55)
print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x=20
print(f"p.x={p.x} and p.y={p.y}")
print(p)
