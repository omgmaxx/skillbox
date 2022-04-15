def get_input_parameters():
    movie_list = []

    amount = int(input('Сколько фильмов хотите добавить? '))

    for i in range(amount):
        movie = str(input(f'Введите название фильма: '))
        movie_list.append(movie)

    return movie_list
    pass


def display_result(favorite_films, errors):
    print()

    for error_movie in errors:
        print(f'Ошибка: фильма {error_movie} у нас нет :(')
    print('\nВаш список любимых фильмов: ')

    for movie in favorite_films:
        print(movie, end=', ')

    pass


def add_favorite_film(new_favorite_films, available_films):
    loved_movies = []
    missing_movies = []

    for movie in new_favorite_films:
        check = 0

        for available_movie in available_films:
            if str(movie) == str(available_movie):
                check = 1

        if check == 1:
            loved_movies.append(movie)
        else:
            missing_movies.append(movie)


    return loved_movies, missing_movies
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
