#!/usr/bin/python3
"""Module for pascale_triangle method."""


def pascal_triangle(n):
    """Return a list of lists of integers representing the pascal triangle of n."""
    if n <= 0:
        return []
    triangles = [1]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp= [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.appen(1)
        triangles.append(tmp)
    return triangles
