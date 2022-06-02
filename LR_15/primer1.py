#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)


if __name__ == '__main__':
    x = Vector2D(3, 4)
    print(x)
    print(abs(x))
    y = Vector2D(5, 6)
    print(y)
    print(x + y)
    print(x - y)
    print(-x)
    x += y
    print(x)
    print(bool(x))
    z = Vector2D(0, 0)
    print(bool(z))
    print(-z)
