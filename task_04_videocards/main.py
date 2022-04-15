def get_input_parameters():
    input_card_list = []
    amount = int(input('Количество видеокарт: '))

    for i in range(amount):
        v_card = int(input(f'{i + 1} Видеокарта: '))
        input_card_list.append(v_card)

    return input_card_list
    pass


def display_result(old_video_cards, new_video_cards):
    print(f'\nСтарый список видеокарт: {old_video_cards}')
    print(f'Новый список видеокарт: {new_video_cards}')

    pass


def select_video_cards(video_cards):
    max_number = 0
    new_card_list = []

    for number in video_cards:
        if number > max_number:
            max_number = number

    for number in video_cards:
        if number != max_number:
            new_card_list.append(number)

    return new_card_list
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
