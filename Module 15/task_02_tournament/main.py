def display_result(participants_names):
    print(f'Список имён участников: {participants_names}')

    pass


def get_participants_names(names):
    count = 0
    even_name_list = []

    for current_name in names:
        if count % 2 == 0:
            even_name_list.append(current_name)
        count += 1

    return even_name_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
