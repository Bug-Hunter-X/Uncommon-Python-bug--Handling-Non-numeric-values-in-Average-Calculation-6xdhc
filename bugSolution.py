def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [1, 2, 3, 'a', 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")
my_list = ['a', 'b', 'c']
average = calculate_average(my_list)
print(f"The average is: {average}")
