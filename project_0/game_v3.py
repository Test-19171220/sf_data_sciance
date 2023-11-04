
import numpy as np

def random_predict(number: int = 1) -> int:
    """Сначала устанавливаем диапазон минимум = 1 и максимум = любому random числу.
    число-предположение устанавливаем равному максимум.
    Далее сравниваем число-предположение с загаданном числом и в зависимости от результата 
    сокращаем диапазон чисел предположений: уменьшаем максимум или увеличиваем минимум.
       
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    mn_predict, mx_predict = 1, np.random.randint(1, 101)
    predict = mx_predict
    while number != predict:
      count += 1
    
      if number > predict:
        mn_predict = predict
        predict = predict + np.random.randint(1, 101)
        
      elif number < predict:
        mx_predict = predict
        predict = (mx_predict + mn_predict ) // 2
       
    return count

#print(game_core_v3())
#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
