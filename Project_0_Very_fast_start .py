import numpy as np

number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
print("Загаданное число:", number)


def game_core_interval(number):
    """Функция задает верхний и нижний интервалы,
       находит их среднее арифметическое и сравнивает его с загаданным числом.
       Если среднее арифметическое меньше загаданного, то среднее
        арифметическое становится новой нижней границей, если больше - верхней.
       Если загаданное число равно 100, то из-за особенностей округления
       среднее арифметическое зациклится в повтор,из-за чего данный случай
       вынесен в исключения в начале проверки.
       Функция принимает загаданное число и возвращает число попыток."""
    guess_attempt = 1
    lower_boundary = 1
    upper_boundary = 100
    mean = int((lower_boundary + upper_boundary) / 2)
    while mean != number:
        guess_attempt += 1
        if mean == 99 and mean != number:
            mean = 100
        elif mean < number:
            lower_boundary = mean
            mean = int((lower_boundary + upper_boundary) / 2)
        elif mean > number:
            upper_boundary = mean
            mean = int((lower_boundary + upper_boundary) / 2)
    return guess_attempt


print("Текущее количество попыток угаадачть число:", game_core_interval(number))


def score_game(game_core):
    """Функция принимает функцию нахождения загаданного числа и выводит среднее
    количество попыток на 1000 разных значений загаданного числа."""
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_list.append(game_core(number))
    score = int(np.mean(count_list))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_interval)
