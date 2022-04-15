def get_input_parameters():

    params = []
    amount = int(input('Количество клеток: '))
    for i in range(amount):
        efficiency = int(input(f'Эффективность {i+1} клетки: '))
        params.append(efficiency)
    return params
    pass


def display_result(cells):

    print('\nНеподходящие значения: ', end='')
    for num in cells:
        print(num, end=' ')
    pass


def select_cells(cells):

    count = 0
    wrong_cells = []
    for cell in cells:
        count += 1
        if cell < count:
            wrong_cells.append(cell)
    return wrong_cells
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
