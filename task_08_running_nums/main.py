def get_input_parameters():
    original_list = input('Изначальный список: ').strip('[]').replace(' ', '').split(',')
    for i in range(len(original_list)):
        original_list[i] = int(original_list[i])

    shift = int(input('Сдвиг: '))
    shift = (abs(shift) % len(original_list)) * (shift**2)  #расчёт сдвига больше списка
    number_list = []
    print('Изначальный список: ', end='')

    return int(shift), original_list
    pass


def display_result(shifted_list):
    print(f'Сдвинутый список: {shifted_list}')
    pass


def shift_list(shift, original_list):
    shifted_list = []
    for x in range(len(original_list)):
        shifted_list.append(original_list[ (x - shift) ])

    return shifted_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    shift, original_list = get_input_parameters()  # получаем параметры
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
