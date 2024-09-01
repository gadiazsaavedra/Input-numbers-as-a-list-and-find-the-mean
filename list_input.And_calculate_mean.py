def create_number_list():
    """
    Prompts the user to enter numbers separated by spaces and returns a
    list of floats.

    Returns:
        list: A list of floats representing the user-input numbers.
    """
    while True:
        try:
            user_input = input("Enter numbers separated by spaces: ").strip()
            if not user_input:
                print("No input provided. Please try again.")
                continue

            numbers = [float(num) for num in user_input.split()]
            print(f"The list of numbers is: {numbers}")
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")


def calculate_mean(numbers: list[float]) -> float:
    """
    Calculate the mean (average) value of a list of numbers.

    Args:
        numbers (list[float]): A list of numbers.

    Returns:
        float: The mean value of the list.
    """
    from statistics import mean

    return mean(numbers)


# Example usage:
number_list = create_number_list()
mean_value = calculate_mean(number_list)
print(f"The mean value of the list is: {mean_value}")

