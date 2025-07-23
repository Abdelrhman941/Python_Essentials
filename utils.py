def greeting(name):
    print(f"Hello, {name}")

def farewell(name):
    print(f"Goodbye, {name}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a * a

def cube(a):
    return a * a * a

def power(a, b):
    return a ** b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst):
    return sorted(lst)

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

def find_min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for item in lst:
        if item < min_value:
            min_value = item
    return min_value

def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

def average(lst):
    if not lst:
        return None
    return sum_list(lst) / len(lst)

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged   

def filter_even_numbers(lst):
    return [item for item in lst if item % 2 == 0]

def filter_odd_numbers(lst):
    return [item for item in lst if item % 2 != 0]

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    return len(s.split())

def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

def find_longest_word(s):
    words = s.split()
    if not words:
        return ""
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def find_shortest_word(s):
    words = s.split()
    if not words:
        return ""
    shortest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word