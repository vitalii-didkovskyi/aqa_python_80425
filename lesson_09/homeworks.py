def factorial(n):
    """
    Обчислює факторіал числа n:
    0! = 1
    1! = 1
    2! = 1·2 = 2
    3! = 1·2·3 = 6
    4! = 1·2·3·4 = 24
    5! = 1·2·3·4·5 = 120
    6! = 1·2·3·4·5·6 = 720
    7! = 1·2·3·4·5·6·7 = 5040
    8! = 1·2·3·4·5·6·7·8 = 40320
    9! = 1·2·3·4·5·6·7·8·9 = 362880
    10! = 1·2·3·4·5·6·7·8·9·10 = 3628800
    """
    if n < 0:
        raise ValueError(f'You have to use 0 or positive numbers. You put {n}')

    if type(n) != int:
        raise TypeError(f'Only int allowed, you put {type(n)}')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1, word2):
    """
    Перевіряє, чи є два рядки анаграмами.
    Анаграма — переставлення літер у слові, завдяки чому утворюється нове значення,
    прочитуване у зворотному напрямку (тік — кіт, мука — кума, літо — тіло).
    """

    return sorted(word1) == sorted(word2)


def filter_even_numbers(lst):
    """
    Фільтрує список, залишаючи тільки парні числа.
    """
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:
    """
    Знаходить усі прості числа:
    Послідовність простих чисел починається так:
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149...
    """
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def triangle_area(a, b, c):
    """
    Обчислює площу трикутника.
    """
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def convert_to_24_hour(time_str):
    """
    Конвертує час з 12-годинного формату в 24-годинний.
    """
    if type(time_str) == list:
        raise TypeError

    if type(time_str) == dict:
        raise ValueError

    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'