def even_numbers(numbers):
  """
  This function takes a list of numbers as an argument and returns a new list with only the even numbers from the original list.

  Args:
      numbers: A list of numbers.

  Returns:
      A new list containing only the even numbers from the original list.
  """
  even_list = []
  for number in numbers:
    if number % 2 == 0:
      even_list.append(number)
  return even_list

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = even_numbers(numbers)
print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]
