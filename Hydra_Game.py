import random
import time

def hydra_game():
    print('''За каждый правильный ответ ты будешь окончательно срубать 1 голову Гидры. 
За неправильный ответ - на месте срубленной головы будут вырастать 2 новых!''')
    head_count = 10

    while head_count > 0:
        print(f'У Гидры {head_count} голов')
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        res = int(input(f'Сколько будет {x} + {y}?: '))
        if res == x + y:
            print('Правильно! Ты срубил одну голову Гидры!')
            head_count -= 1
        else:
            print('Не правильно! На месте срубленной головы выросли 2!')
            head_count += 1

    if head_count == 0:
        print('Поздравляем! Вы победили!')
        z = input('Желате начать игру заново? yes or no: ')
        if z == 'yes':
            hydra_game()
        else:
            exit()

if __name__ == '__main__':
    print('Приветствую тебя, воин! Ты пришел сразиться с ужасной Гидрой!')
    begin = input('Если ты готов начать, напечатай "start". Для выхода напечатай "exit" :')
    if begin == 'start':
        hydra_game()
    else:
        exit()
