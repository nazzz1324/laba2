import random, os, time

rules = {
    "камень": {"ножницы"},
    "бумага": {"камень"},
    "ножницы": {"бумага"},
}

def play(computer):
    '''
    Функция запуска и завершения игры "камень, ножинцы, бумага"
    '''
    print("Добро пожаловать в игру камень, ножницы, бумага!!")

    while True:
        player = player_input()
        print(f"Ваш выбор: {player}")

        if player == "stop":
            print("Игра завершена!!!")
            break

        print(f"Ваш выбор: {player}")
        print(f"Выбор компьютера: {computer}")

        if player in rules[computer]:
            print("Выйграл компьютер!!!")

        if computer in rules[player]:
            print("Вы выйграли!!!")

        if computer == player:
            print("Ничья!!!")

        #Это для очистки терминала, после оглашения результатов каждой игры после прохождения 5 секунд
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')



choices = ["камень", "ножницы", "бумага"]
def step_computer():
    '''
        Функция выбора хода компьютера
    '''
    return random.choice(choices)

def player_input():
    '''
            Функция запрашивающая выбора хода у игрока
    '''
    while True:
        player = input("Выберите: камень, ножницы, бумага, либо stop для завершения игры: ").lower()
        if player in choices or player =="stop":
            return player
            break

        else:
            print("Некорректный ввод. Повторите ввод.")




play(computer= step_computer())

