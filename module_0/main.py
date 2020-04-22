def game_core_v2(number):
    '''Отказываемся от случайного начального значения, начинаем с середины диапазона 
    predict = 50. В среднем, никакой разницы по количеству шагов, нужных для отгадывания числа нет'''
    count = 1
    imax = 100
    imin = 1
    predict = 50 #np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: #загаданное число больше прогноза
            imin = predict
            predict = int((imax + predict)/2)   #делим диапазон на 2
            if predict == imin and (predict+1) <= imax:
                predict+=1
            elif predict == imin and (predict+1) > imax:
                return(-1) #ошибка алгоритма
        elif number < predict:  #загаданное число меньше прогноза
            imax = predict
            predict = int((predict + imin)/2) #делим диапазон на 2
            if predict == imax and (predict-1) >= imin:
                predict-=1
            elif predict == imin and (predict-1) < imax:
                return(-1) #ошибка алгоритма
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core_v2)