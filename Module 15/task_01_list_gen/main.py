def get_input_parameters():
    N = int(input('Введите число N: '))
    return N
    pass


def display_result(odd_numbers):
    print(f'\nСписок из нечётных чисел от одного до N: {list(odd_numbers)}')
    pass


def get_odd_numbers(number):
    odd_num_list = []
    for i in range(1, number + 1, 2):
        odd_num_list.append(i)
    return odd_num_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
