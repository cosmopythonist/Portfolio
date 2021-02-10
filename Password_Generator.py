import random

def generate_password(length, chars):
    psw = ''
    for i in range(length):
        psw += random.choice(chars)
    return psw

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punktuation = '!#$%&*+-=?@^_'

chars = []

count_pass = int(input('Сколько паролей вы хотите сгенерировать? :> '))
len_pass = int(input('Укажите длину пароля :> '))
digit_on = input('Включать цифры в пароль? Да или Нет:> ').lower()
low_letter_on = input('Включать маленькие буквы? Да или Нет :> ').lower()
up_letter_on = input('Включать большие буквы? Да или Нет :> ').lower()
punk_on = input('Включать символы? Да или Нет :> ').lower()

if digit_on == 'да':
    chars += list(digits)
if low_letter_on == 'да':
    chars += list(lowercase_letters)
if up_letter_on == 'да':
    chars += list(uppercase_letters)
if punk_on == 'да':
    chars += list(punktuation)

print('Пароли успешно сгенерированы.')
for i in range(count_pass):
    print(generate_password(len_pass, chars))