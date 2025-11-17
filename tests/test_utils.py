import pytest
from main import *

class TestPalindrome:
    def test_kajak(self):
        assert is_palindrome('kajak') is True
    def test_kobyla(self):
        assert is_palindrome('Kobyła ma mały bok') is True
    def test_python(self):
        assert is_palindrome('python') is False
    def test_empty(self):
        assert is_palindrome("") is True
    def test_a(self):
        assert is_palindrome('A') is True

class TestFibonacci:
    def test_fib_0(self):
        assert fibonacci(0) == 0
    def test_fib_1(self):
        assert fibonacci(1) == 1
    def test_fib_5(self):
        assert fibonacci(5) == 5
    def test_fib_55(self):
        assert fibonacci(10) == 55
    def test_fib_1m(self):
        assert fibonacci(-1) is None

class TestVowels:
    def test_vowels_python(self):
        assert count_vowels('Python') == 2
    def test_vowels2(self):
        assert count_vowels('AEIOUY') == 6
    def test_vowels_3(self):
        assert count_vowels('bcd') == 0
    def test_vowels_empty(self):
        assert count_vowels('') == 0
    def test_vowels_turtle(self):
        assert count_vowels('Próba żółwia') == 5

class TestDiscount:
    def test_discount_0(self):
        assert calculate_discount(100, 0.2) == 80.0
    def test_discount_1(self):
        assert calculate_discount(50, 0) == 50.0
    def test_discount_2(self):
        assert calculate_discount(200, 1) == 0.0
    def test_discount_3(self):
        with pytest.raises(ValueError):
            calculate_discount(100, -0.1)
    def test_discount_4(self):
        with pytest.raises(ValueError):
            calculate_discount(100, 1.5)

class TestFlattenList:
    def test_flatten_simple(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_flatten_nested(self):
        assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]

    def test_flatten_empty(self):
        assert flatten_list([]) == []

    def test_flatten_deep_nested(self):
        assert flatten_list([[[1]]]) == [1]

    def test_flatten_mixed(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


class TestWordFrequencies:
    def test_to_be_or_not_to_be(self):
        result = word_frequencies("To be or not to be")
        assert result == {"to": 2, "be": 2, "or": 1, "not": 1}

    def test_hello_hello(self):
        result = word_frequencies("Hello, hello!")
        assert result == {"hello": 2}

    def test_empty(self):
        result = word_frequencies("")
        assert result == {}

    def test_python_variants(self):
        result = word_frequencies("Python Python python")
        assert result == {"python": 3}

    def test_punctuation_and_polish(self):
        result = word_frequencies("Ala ma kota, a kot ma Ale.")
        assert result["ala"] == 1
        assert result["ma"] == 2
        assert result["kota"] == 1
        assert result["kot"] == 1
        assert result["a"] == 1
        assert result["ale"] == 1

class TestIsPrime:
    def test_prime_2(self):
        assert is_prime(2) is True

    def test_prime_3(self):
        assert is_prime(3) is True

    def test_not_prime_4(self):
        assert is_prime(4) is False

    def test_not_prime_0(self):
        assert is_prime(0) is False

    def test_not_prime_1(self):
        assert is_prime(1) is False

    def test_prime_5(self):
        assert is_prime(5) is True

    def test_prime_97(self):
        assert is_prime(97) is True