import numpy as np


def random_predict(number):
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break

    return count


def game_core_v2(number):
    count = 0
    predict_number = np.random.randint(1, 101)

    while number != predict_number:
        count += 1
        if number > predict_number:
            predict_number += 1
        elif number < predict_number:
            predict_number -= 1

    return count


def game_core_v3(number):
    count = 0
    max_num = 101
    min_num = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            min_num = predict
            predict = np.random.randint(min_num, max_num)
        elif number < predict:
            max_num = predict
            predict = np.random.randint(min_num, max_num)

    return count


def score_game(random_predict):
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=10000)

    for number in random_array:
        count_list.append(random_predict(number))

    score = int(np.mean(count_list))
    print(f"Your algorithm guesses the number on average for: {score} attempts")


print("random_predict")
score_game(random_predict)
print("game_core_v2")
score_game(game_core_v2)
print("game_core_v3")
score_game(game_core_v3)