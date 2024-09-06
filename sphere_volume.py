import math


def get_number() -> float:
    """
    Prompts the user to enter a number and returns it as a float.

    Returns:
        float: The number entered by the user.

    Raises:
        ValueError: If the user enters an invalid input.
    """
    while True:
        user_input = input("Enter a number: ").strip()
        if not user_input:
            print("No input provided. Please try again.")
            continue

        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")


def sphere_volume(radius: float) -> float:
    """
    Calculate the volume of a sphere.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.

    Raises:
        ValueError: If the radius is non-positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")

    pi = math.pi
    return (4 / 3) * pi * (radius**3)


def main():
    """
    The main function to calculate the volume of a sphere.
    """
    radius = get_number()
    try:
        volume = sphere_volume(radius)
        print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
