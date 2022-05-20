import unittest

from main import RandomValuesStats
inta = RandomValuesStats()

lista_1 = [10, 100, 500, 1000]
lista_2 = [-10, -100, -500, -1000]
lista_3 = [2, 4, 17, 25]
prime_list = [2, 11, 23, 44]


class TestMaximumValue(unittest.TestCase):
    def test_maximum_value(self):
        for num in lista_1:
            inta.update_max_if_greater(num)
        self.assertEqual(inta.max_number, 1000)
        inta.set_default_values()

    def test_maximum_value_with_negative_numbers(self):
        for num in lista_2:
            inta.update_max_if_greater(num)
        self.assertEqual(inta.max_number, -10)
        inta.set_default_values()

    def test_try_maximum_value_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_max_if_greater(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_maximum_value_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_max_if_greater("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestMinimumValue(unittest.TestCase):
    def test_minimum_value(self):
        for num in lista_1:
            inta.update_min_if_lower(num)
        self.assertEqual(inta.min_number, 10)
        inta.set_default_values()

    def test_minimum_value_with_negative_numbers(self):
        for num in lista_2:
            inta.update_min_if_lower(num)
        self.assertEqual(inta.min_number, -1000)
        inta.set_default_values()

    def test_try_minimum_value_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_min_if_lower(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_minimum_value_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_min_if_lower("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestFirstValue(unittest.TestCase):
    def test_first_value(self):
        for num in lista_1:
            inta.set_first(num)
        self.assertEqual(inta.first_number, 10)
        inta.set_default_values()

    def test_first_value_with_negative_numbers(self):
        for num in lista_2:
            inta.set_first(num)
        self.assertEqual(inta.first_number, -10)
        inta.set_default_values()

    def test_try_first_value_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.set_first(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_first_value_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.set_first("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestLastValue(unittest.TestCase):
    def test_last_value(self):
        for num in lista_1:
            inta.set_last(num)
        self.assertEqual(inta.last_number, 1000)
        inta.set_default_values()

    def test_last_value_with_negative_numbers(self):
        for num in lista_2:
            inta.set_last(num)
        self.assertEqual(inta.last_number, -1000)
        inta.set_default_values()

    def test_try_last_value_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.set_last(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_last_value_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.set_last("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestPrimeValue(unittest.TestCase):
    def test_count_prime_numbers(self):
        for num in prime_list:
            inta.update_prime_counter(num)
        self.assertEqual(inta.number_of_prime_numbers, 3)
        inta.set_default_values()

    def test_try_count_prime_numbers_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_prime_counter(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_count_prime_numbers_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.set_last("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestEvenAndOddValue(unittest.TestCase):
    def test_count_even_and_odd_numbers(self):
        for num in lista_3:
            inta.update_odd_or_even_counter(num)
        self.assertEqual(inta.number_of_even_numbers, 2)
        self.assertEqual(inta.number_of_odd_numbers, 2)
        inta.set_default_values()

    def test_count_even_and_odd_numbers_negative_numbers(self):
        for num in lista_2:
            inta.update_odd_or_even_counter(num)
        self.assertEqual(inta.number_of_even_numbers, 4)
        self.assertEqual(inta.number_of_odd_numbers, 0)
        inta.set_default_values()

    def test_try_count_prime_numbers_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_odd_or_even_counter(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])

    def test_try_count_prime_numbers_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.update_odd_or_even_counter("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])


class TestCallFunctions(unittest.TestCase):
    def test_call_functions(self):
        for num in range(1, 50):
            inta.take_sample(num)
        self.assertEqual(inta.max_number, 49)
        self.assertEqual(inta.min_number, 1)
        self.assertEqual(inta.first_number, 1)
        self.assertEqual(inta.last_number, 49)
        self.assertEqual(inta.number_of_even_numbers, 24)
        self.assertEqual(inta.number_of_odd_numbers, 25)
        self.assertEqual(inta.number_of_prime_numbers, 15)
        inta.set_default_values()

    def test_try_call_functions_with_none_value(self):
        with self.assertRaises(Exception) as context:
            inta.take_sample(None)
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])
    
    def test_try_call_functions_with_string_value(self):
        with self.assertRaises(Exception) as context:
            inta.take_sample("abc")
        self.assertEqual(
            "That was no valid number.",
            context.exception.args[0])



if __name__ == '__main__':
    unittest.main()
