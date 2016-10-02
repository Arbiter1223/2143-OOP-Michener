# Bare minimum
class pnt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Recommended

# Usage
# p1 = point(3, 5)
# p1.move(-1, -1)
# p1.setx(5)
# p1.sety(3)
class Point(object):
    def __init__(self, x = None, y = None):
        if x:
            self.x = x
        else:
            self.x = 0

        if y:
            self.y = y
        else:
            self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y

    def setx(self, x):
        self.x = x

    def sety (self, y):
        self.y = y