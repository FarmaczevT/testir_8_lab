import unittest
from lab1 import Labs1

class TestLabs1(unittest.TestCase):
# тесты 1 функции
    # тест проверяет правильность сортировки массива целых чисел
    def test_bubble_sort(self):
        arr = [5, 3, 1, 4, 2]
        expected = [1, 2, 3, 4, 5]
        result = Labs1.bubble_sort(arr)
        self.assertEqual(expected, result)
    # тест проверяет ситуацию, когда входной массив пустой
    def test_bubble_sort_empty_array(self):
        arr = []
        with self.assertRaises(Exception) as context:
            Labs1.bubble_sort(arr)
        self.assertEqual("Ошибка: Пустой массив!", str(context.exception))
    # тест проверяет массив на содержание недопустимых элементов (строки)
    def test_bubble_sort_with_non_integer_element(self):
        arr = [4, 2, 7, 1, "9"]
        with self.assertRaises(Exception) as context:
            Labs1.bubble_sort(arr)
        self.assertEqual(str(context.exception), "Вводите только целые числа!")
# тесты 2 функции
    # тест проверяет, правильно ли функция is_palindrome определяет, является ли слово палиндромом
    def test_is_palindrome_valid_palindrome(self):
        string = "мадам"
        result = Labs1.is_palindrome(string)
        self.assertEqual(True, result)
    # тест проверяет, правильно ли функция is_palindrome определяет, является ли слово палиндромом
    def test_is_palindrome_not_palindrome(self):
        string = "хрюшка"
        result = Labs1.is_palindrome(string)
        self.assertEqual(False, result)
    # тест проверяет, как функция is_palindrome обрабатывает случай пустой строки
    def test_is_palindrome_empty_string(self):
        string = " "
        with self.assertRaises(Exception) as context:
            Labs1.is_palindrome(string)
        self.assertEqual("Нельзя вводить пустые значения!", str(context.exception))
    # тест проверяет, как функция is_palindrome обрабатывает случай строки с недопустимыми символами
    def test_is_palindrome_string_with_non_alpha_chars(self):
        string = "Яблоки, aнанасы, мороженое, конфетки!"
        with self.assertRaises(Exception) as context:
            Labs1.is_palindrome(string)
        self.assertEqual("Нельзя вводить символы и знаки препинания!", str(context.exception))
# тесты 3 функции
    # тест проверяет, правильно ли функция factorial вычисляет факториал положительного целого числа
    def test_factorial_valid_input(self):
        n = 5
        result = Labs1.factorial(n)
        self.assertEqual(120, result)
    # тест проверяет, как функция factorial обрабатывает случай отрицательного целого числа
    def test_factorial_negative_input(self):
        n = -2
        with self.assertRaises(Exception) as context:
            Labs1.factorial(n)
        self.assertEqual("Факториал определен только для неотрицательных чисел", str(context.exception))
    # тест проверяет, как функция factorial обрабатывает случай, когда входной аргумент является строкой
    def test_factorial_invalid_input_string(self):
        string = "abc"
        with self.assertRaises(Exception) as context:
            Labs1.factorial(string)
        self.assertEqual("Аргумент должен быть целым числом", str(context.exception))
# тесты 4 функции
    # тест проверяет, правильно ли функция fibonacci вычисляет число Фибоначчи для положительных целых чисел
    def test_fibonacci_valid_input(self):
        n = 6
        result = Labs1.fibonacci(n)
        self.assertEqual(8, result)
    # тест проверяет, как функция fibonacci обрабатывает случай отрицательного целого числа
    def test_fibonacci_negative_input(self):
        n = -3
        with self.assertRaises(Exception) as context:
            Labs1.fibonacci(n)
        self.assertEqual("Позиция должна быть неотрицательным целым числом", str(context.exception))
    # тест проверяет, как функция fibonacci обрабатывает случай, когда входной аргумент является пустой строкой
    def test_fibonacci_invalid_input_empty_string(self):
        string = ""
        with self.assertRaises(Exception) as context:
            Labs1.fibonacci(string)
        self.assertEqual("Аргумент не может быть пустым", str(context.exception))
# тесты 5 функции
    # тест проверяет, правильно ли функция exp () вычисляет степень целого числа
    def test_exp_valid_input(self):
        base = 2
        exponent = 3
        result = Labs1.exp(base, exponent)
        self.assertEqual(8, result)
    # тест проверяет, как функция exp () обрабатывает случай, когда основание является числом, а показатель степени - строкой
    def test_exp_invalid_input(self):
        base = 2
        exponent = "3"
        with self.assertRaises(Exception) as context:
            Labs1.exp(base, exponent)
        self.assertEqual("Аргументы должны быть числами", str(context.exception))
    # тест проверяет, как функция exp () обрабатывает случай, когда основание и показатель степени являются пустотой
    def test_exp_invalid_empty_input(self):
        base = ""
        exponent = ""
        with self.assertRaises(Exception) as context:
            Labs1.exp(base, exponent)
        self.assertEqual("Аргументы должны быть числами", str(context.exception))
# тесты 6 функции
    # проверяет, правильно ли функция is_simple () определяет, что число 7 является простым числом
    def test_is_simple_number(self):
        number = 7
        result_message = Labs1.is_simple(number)
        self.assertEqual("7 является простым числом", result_message)
    # тест проверяет, как функция is_simple () обрабатывает случай, когда число 12 не является простым числом
    def test_is_not_simple_number(self):
        number = 12
        result_message = Labs1.is_simple(number)
        self.assertEqual("12 не является простым числом", result_message)
    # тест проверяет, как функция is_simple () обрабатывает случай, когда входной аргумент является числом с плавающей точкой
    def test_is_simple_non_integer_input(self):
        number = 5.5
        with self.assertRaises(Exception) as context:
            Labs1.is_simple(number)
        self.assertEqual("Аргумент должен быть целым числом", str(context.exception))

if __name__ == '__main__':
    unittest.main()