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
