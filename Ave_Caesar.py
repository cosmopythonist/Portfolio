def encryption(fraza):
    shifr = []
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    el = ''
    count = 0
    for i in range(len(fraza)):
        for e in fraza[i]:
            if e.isalpha():
                count += 1
        for c in fraza[i]:
            if c.isalpha():
                if c == c.upper():
                    for j in range(0, len(up)):
                        if c == up[j]:
                            el += up[(j + count) % 26]
                else:
                    for j in range(0, len(low)):
                        if c == low[j]:
                            el += low[(j + count) % 26]
            else:
                el += c

        if len(el) == len(fraza[i]):
            shifr.append(el)
            el = ''
            count = 0
            continue
    return print(' '.join(shifr))

if __name__ == '__main__':
    fraza = input('Введите фразу, которую желаете зашифровать :> ').split(' ')
    encryption(fraza)