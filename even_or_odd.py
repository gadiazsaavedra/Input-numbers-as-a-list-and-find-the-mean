def get_number() -> int:
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
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")

def even_or_odd(user_input: int) -> str:
    """
    Determine if a number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: 'even' or 'odd'
    """
    return 'even' if user_input % 2 == 0 else 'odd'

def main():
    """
    The main function to calculate the volume of a sphere.
    """
    radius = get_number()
    try:
        volume = even_or_odd(radius)
        print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
