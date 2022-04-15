def get_input_parameters():
    word = str(input('Введите слово: '))

    return word
    pass


def display_result(number_unique_letters):
    print('\nКоличество уникальных букв: ', number_unique_letters)
    pass


def count_number_unique_letters(word):
    letters = list(word)
    uniques = len(letters)

    for x in range(len(letters)):
        for y in range(len(letters)):
            if letters[x] == letters[y] and x != y:
                uniques -= 1

    return uniques
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
