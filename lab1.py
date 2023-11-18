class Labs1:
    @staticmethod
    def bubble_sort(arr):
        # Проверка на целые числа
        for item in arr:
            if not isinstance(item, int):
                raise Exception("Вводите только целые числа!")
        # Проверка на пустоту
        if len(arr) == 0:
            raise Exception("Ошибка: Пустой массив!")
            
        n = len(arr)   
        for i in range(n): #  количество итераций цикла сортировки
            for j in range(n - i - 1): # игнорируем последнии i элементы, которые уже отсортировались
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    @staticmethod
    def is_palindrome(string):
        # Проверка на пустоту
        if not string.strip():
            raise Exception("Нельзя вводить пустые значения!")
        
        # Проверка на символы и знаки препинания
        if not string.isalpha():
            raise Exception("Нельзя вводить символы и знаки препинания!")
        
        # Удаляем пробелы из строки и приводим все символы к нижнему регистру
        cleaned_string = string.replace(" ", "").lower()
        # Сравниваем очищенную строку с ее перевернутой версией
        if cleaned_string == cleaned_string[::-1]:
            return True
        else:
            return False
        
        
    @staticmethod
    def factorial(n):
        # Проверка на пустоту
        if n is None:
            raise Exception("Аргумент не может быть пустым")

        # Проверка на тип аргумента
        if not isinstance(n, int):
            raise Exception("Аргумент должен быть целым числом")

        # Проверка на отрицательное значение
        if n < 0:
            raise Exception("Факториал определен только для неотрицательных чисел")
        
        if n == 0:
            return 1
        else:
            return n * Labs1.factorial(n-1)
        
    @staticmethod
    def fibonacci(n):
        # Проверка на пустоту
        if n == "":
            raise Exception("Аргумент не может быть пустым")
        # Проверка на тип аргумента
        if not isinstance(n, int):
            raise Exception("Аргумент должен быть целым числом")
        # Проверка на отрицательное значение
        if n < 0:
            raise Exception("Позиция должна быть неотрицательным целым числом")

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_prev = 0
            fib_curr = 1
            for i in range(2, n+1):
                fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
            return fib_curr
        
    @staticmethod
    def exp(base, exponent):
        if not isinstance(base, (float, int)) or not isinstance(exponent, (float, int)):
            raise Exception("Аргументы должны быть числами")
    
        result = float(base) ** float(exponent)
        return result
    
    @staticmethod
    def is_simple(number):
        if not isinstance(number, int):  # проверка типа объекта
            raise Exception("Аргумент должен быть целым числом")
        
        if number < 2:
            return (number, "не является простым числом")

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return (f"{number} не является простым числом")
        
        return (f"{number} является простым числом")


# # Пример использования
# print("1 задание")
# arr = [2, 3, 4, 2, 2, 11, 12]
# bubble_sort = Labs1.bubble_sort(arr)
# print(bubble_sort)  # Вывод отсортированного массива

# bubble_sort = Labs1.bubble_sort([])  # Попытка сортировки пустого массива
# print(bubble_sort)  # Вывод сообщения "Нельзя ввести пустоту."

# bubble_sort = Labs1.bubble_sort([2, 3, 4, 2, "5", 11, 12])  # Попытка сортировки массива с нецелыми числами
# print(bubble_sort)  # Вывод сообщения "Вводите только целые числа."
# print("\n")

# print("2 задание")
# valid_palindrome = Labs1.is_palindrome("Мадам")
# print(valid_palindrome)  # Вывод True (палиндром игнорируя символы и регистр)

# valid_palindrome = Labs1.is_palindrome("Привет")
# print(valid_palindrome)  # Вывод True (палиндром игнорируя символы и регистр)

# invalid_empty = Labs1.is_palindrome("  ")
# print(invalid_empty)  # Вывод сообщения "Нельзя вводить пустые значения."

# invalid_symbols = Labs1.is_palindrome("//??")
# print(invalid_symbols)  # Вывод сообщения "Нельзя вводить символы и знаки препинания."
# print("\n")

# print("3 задание")
# factorial = Labs1.factorial(5)
# print(factorial)  # Вывод 120

# factorial_empty = Labs1.factorial(" ")
# print(factorial_empty)  # Вывод Аргумент должен быть целым числом

# factorial = Labs1.factorial("asdasd")
# print(factorial)  # Вывод Аргумент должен быть целым числом

# invalid_symbols = Labs1.factorial(-12)
# print(invalid_symbols)  # Вывод Факториал определен только для неотрицательных чисел
# print("\n")

# print("4 задание")
# fibonacci = Labs1.fibonacci(0)
# print(fibonacci)  # Вывод 5

# fibonacci = Labs1.fibonacci(5.2)
# print(fibonacci)  # Аргумент должен быть целым числом

# fibonacci = Labs1.fibonacci("sdsdsd")
# print(fibonacci)  # Аргумент должен быть целым числом

# fibonacci = Labs1.fibonacci("")
# print(fibonacci)  # Вывод Аргумент должен быть целым числом

# fibonacci = Labs1.fibonacci(-12)
# print(fibonacci)  # Позиция должна быть положительным целым числом
# print("\n")

# print("5 задание")
# expon = Labs1.exp(2.2, 2.2)
# print(expon)  # Вывод: 5.666

# expon = Labs1.exp("",2)
# print(expon)  # Вывод: Поля не должны быть пустыми

# expon = Labs1.exp(2.5, "abc")
# print(expon)  # Вывод: Поля должны содержать числа 
# print("\n")

# print("6 задание")
# is_simple_result = Labs1.is_simple(-11)
# print(is_simple_result)  # Вывод: Число меньше 2, не может быть простым

# is_simple_result = Labs1.is_simple(2)
# print(is_simple_result)  # Вывод: Простое число

# is_simple_result = Labs1.is_simple(21)
# print(is_simple_result)  # Вывод: Не Простое число

# is_simple_result = Labs1.is_simple(21.2)
# print(is_simple_result)  # Вывод: Аргумент должен быть целым числом

# is_simple_result = Labs1.is_simple("sdds")
# print(is_simple_result)  # Вывод: Аргумент должен быть целым числом

# is_simple_result = Labs1.is_simple(" ")
# print(is_simple_result)  # Вывод: Аргумент должен быть целым числом
# print("\n")