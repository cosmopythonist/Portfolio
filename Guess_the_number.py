import random

print('Добро пожаловать в числовую угадайку!')

def is_valid(s, d):
    if s.isdigit() and 1 <= int(s) <= d:
        return True
    else:
        return False

def game():
    d = int(input('Укажите правую границу для выбора числа. От 1 до ? :> '))
    num = random.randint(1, d)

    flag = True
    count = 0
    while flag == True:
        s = input(f'Введите число от 1 до {d} :> ')
        if is_valid(s, d):
            s = int(s)
            count += 1
            if s < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            if s > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            if s == num:
                print('Вы угадали, поздравляем!')
                print(f'Количество попыток = {count}')
                flag = False
        else:
            print(f'А может быть все-таки введем целое число от 1 до {d}?')
            continue

if __name__ == '__main__':
    game()
    while True:
        z = input('Отличная игра! Может еще раз? Да или Нет? :> ')
        if z.lower() == 'да':
            game()
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
