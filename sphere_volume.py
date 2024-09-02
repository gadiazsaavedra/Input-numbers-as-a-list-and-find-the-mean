import math

"""The volume of a sphere is given by (4/3 * pi * r3).
Calculate the volume of a sphere of radius 5.
Suggestion: create a variable named “pi” with the value of 3.1415."""


def sphere_volume(radius):
    """
    Calculate the volume of a sphere.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    pi = math.pi
    return (4 / 3) * pi * (radius**3)
