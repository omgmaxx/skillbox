def get_input_parameters():
    container_list = []
    last_container = 200   #ограничитель

    amount = int(input('Количество контейнеров: '))

    for i in range(amount):
        container = int(input('Введите вес контейнера: '))
        while container > last_container:   #контейнер <= ограничителя или пред. контейнера
            container = int(input('Ошибка ввода: нарушен порядок убывания. Повторите: '))
        else:
            container_list.append(container)
            last_container = container

    new_container_weight = int(input('\nВведите вес нового контейнера: '))

    return container_list, new_container_weight
    pass


def display_result(serial_number_new_container):
    print('\nНомер, который получит новый контейнер:', serial_number_new_container)
    pass


def search_serial_number_new_container(list_container_weights, new_container_weight):
    count = 0
    for i_weight in list_container_weights:
        count += 1
        if i_weight <= new_container_weight:   #поиск номера контейнера >= добавляемого
            break

    return count
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    list_container_weights, new_container_weight = get_input_parameters()  # получаем параметры
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
