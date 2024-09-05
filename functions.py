# functions.py

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

def reverse_string(text):
    """Returns the reversed version of the input string."""
    return text[::-1]

def count_vowels(text):
    """Returns the count of vowels in the input string, ignoring case sensitivity."""
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

def calculate_factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def decorator_func(func):
    """Decorator that prints a message before calling the original function."""
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """Applies the decorator_func to the input function."""
    return decorator_func(func)

def sort_by_age(list_of_tuples):
    """Sorts a list of tuples by the age (second element) in ascending order."""
    return sorted(list_of_tuples, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    """Merges two dictionaries. Sums up values for common keys."""
    merged_dict = dict1.copy()  # Start with the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
