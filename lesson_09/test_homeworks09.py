import unittest
from homeworks import (
    factorial,
    is_anagram,
    filter_even_numbers,
    find_primes,
    triangle_area,
    convert_to_24_hour)

class MyTest(unittest.TestCase):

    def test_1_factorial_positive(self):
        """
        Тестування функції обчислення факторіалу - позитивні кейси:
            0! = 1
            1! = 1
            2! = 1·2 = 2
            3! = 1·2·3 = 6
        """

        self.assertEqual(factorial(0), 1, "Факторіал 0 має бути 1")
        self.assertEqual(factorial(1), 1, "Факторіал 1 має бути 1")
        self.assertEqual(factorial(3), 6, "Факторіал 3 має бути 6")

    def test_2_factorial_negative(self):
        """
        Тестування функції обчислення факторіалу - негативні кейси:
            str - TypeError;
            >0 - ValueError;
            float - TypeError;
        """

        with self.assertRaises(TypeError):
            factorial("3")
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(1.5)

    def test_3_is_anagram_positive(self):
        """
        Тестування функції визначення анаграми - позитивні кейси.
        """

        self.assertTrue(is_anagram("homework", "homework"), "однакові слова - анаграма")
        self.assertTrue(is_anagram("cat", "act"), "cat та act - анаграма")

    def test_4_is_anagram_negative(self):
        """
        Тестування функції визначення анаграми - негативні кейси.
        """

        self.assertFalse(is_anagram("my", "name"), " 'my' та 'name' не є анаграмами")

    def test_5_filter_even_numbers_positive(self):
        """
        Тестування функції пошуку парних чисел - позитивні кейси.
        """
        self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6], "Всі парні числа мають залишитися")
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([1, 2.0, 4.0]), [2, 4], "2 та 4")

    def test_6_filter_even_numbers_negative(self):
        """
        Тестування функції пошуку парних чисел - негативні кейси.
        """
        self.assertEqual(filter_even_numbers([0, 2.0, 4.0]), [0, 2, 4])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [], "має повертати порожній список")


    def test_7_find_primes(self):
        """
        Тестування функції пошуку простих чисел.
        """

        self.assertEqual(find_primes(10), [2, 3, 5, 7])
        self.assertEqual(find_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(find_primes(2), [2])
        self.assertEqual(find_primes(1), [], "До 1 немає простих чисел")

    def test_8_triangle_area(self):
        """
        Тестування функції обчислення площі трикутника.
        """

        self.assertAlmostEqual(triangle_area(2, 2, 2), 1.7320508075688772)
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6)
        self.assertAlmostEqual(triangle_area(2, 4, 6), 0)

    def test_9_convert_to_24_hour_positive(self):
        """
        Тестування функції конвертації часу в 24-годинний формат - позитивні кейси.
        """

        self.assertEqual(convert_to_24_hour("08:30 AM"), "08:30")
        self.assertEqual(convert_to_24_hour("12:00 PM"), "12:00")
        self.assertEqual(convert_to_24_hour("01:45 PM"), "13:45")

    def test_10_convert_to_24_hour_negative(self):
        """
        Тестування функції конвертації часу в 24-годинний формат - негативні кейси.
        """

        with self.assertRaises(TypeError):
            convert_to_24_hour([])
        with self.assertRaises(ValueError):
            convert_to_24_hour({})
        with self.assertRaises(ValueError):
            convert_to_24_hour("08 AM")
        with self.assertRaises(ValueError):
            convert_to_24_hour("08:00")


if __name__ == '__main__':
    print('Test gonna started')
    unittest.main(verbosity=2)
