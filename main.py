import re


def is_palindrome(text: str) -> bool:
    clean_text = text.lower().replace(' ', '')
    for i in range(len(clean_text)//2):
        if clean_text[i] != clean_text[-(i+1)]:
            return False
    return True

def fibonacci(n):
    if n < 0:
        return None
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def count_vowels(text: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'ó', 'y', 'ą', 'ć', 'ń', 'ę']
    counter = 0

    for i in range(len(text)):
        if text[i].lower() in vowels:
            counter += 1
    return counter

print(count_vowels('python'))

def calculate_discount(price: float, discount: float) -> float:
    if discount > 1 or discount < 0:
        raise ValueError('discount must be between 0 and 1')
    return price - (price * discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result


def word_frequencies(text: str) -> dict:
    if not text:
        return {}

    cleaned = re.sub(r'[^\w\s]', ' ', text.lower())
    words = cleaned.split()

    freqs = {}
    for word in words:
        freqs[word] = freqs.get(word, 0) + 1
    return freqs

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True