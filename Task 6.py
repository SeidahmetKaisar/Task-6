numbers = input("Введите числа через пробел: ")
try:
    number_list = [float(num) for num in numbers.split()]

    if len(number_list) == 0:
        print("Вы не ввели ни одного числа. Попробуйте снова.")
    else:
        average = sum(number_list) / len(number_list)
        print(f"Среднее значение: {average}")
except ValueError:
    print("Ошибка: введите только числа, разделённые пробелами.")
