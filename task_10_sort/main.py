def get_input_parameters():
    original_list = input('Изначальный список: ').strip('[]').replace(' ', '').split(',')
    for i in range(len(original_list)):
        original_list[i] = int(original_list[i])
    print()
    return original_list
    pass


def display_result(sorted_list):

    print(f'Отсортированный список: {sorted_list}')
    pass


def sort_list(original_list):
    for i in range(len(original_list)-1):
        min = original_list[i]
        coun_index = i
        for j in range(i+1, len(original_list) -1 ):
            if min > original_list[j]:
                min = original_list[j]
                coun_index = j
        original_list[i], original_list[coun_index] = original_list[coun_index], original_list[i]
    return original_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
