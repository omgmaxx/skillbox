def get_input_parameters():
    word = str(input('Введите слово: '))

    return word
    pass


def display_result(is_palindrome):
    if is_palindrome == True:
        print('\n\nСлово является палиндромом')
    else:
        print('\n\nСлово не является палиндромом')

    pass


def check_palindrome(word):
    word_list = list(word)
    check = True

    for x in range(len(word_list)):
        y = len(word_list)-1 - x
        if word_list[x] != word_list[y]:
            check = False
            break

    return check
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
