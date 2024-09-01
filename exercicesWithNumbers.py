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


# Example usage
numbers = 2, 4
mean_value = calculate_mean(numbers)
print(f"The mean value is: {mean_value}")

# resultado: float = statistics.mean([12, (14/6), 15])
# print(f"The mean value is: {resultado}")
###################################
