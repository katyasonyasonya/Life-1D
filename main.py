print('Привет! Добро пожаловать в игру «Жизнь 1D». Желаем удачи!')
c = '1'
while c == '1':
    print('Введите длину мира')
    a1 = int(input())
    a = list(a1 * ' ')
    a2 = list(a1 * ' ')
    print('Введите номера ячеек, в которых вы бы хотели зародить жизнь, через пробел (номер не должен быть больше длины мира)')
    b = input().split()
    for i in b:
        a[int(i) - 1] = '#'
        a2[int(i) - 1] = '#'
    print('Введите количество поколений')
    p = int(input())
    print('0)' + ''.join(a))
    for j in range(p):
        for i in range(len(a)):
            if i != len(a) - 1:
                if a[i - 1] == '#' and a[i + 1] == '#':
                    a2[i] = ' '
                elif a[i - 1] == ' ' and a[i + 1] == ' ':
                    a2[i] = ' '
                elif a[i - 1] == '#' and a[i + 1] == ' ':
                    a2[i] = '#'
                elif a[i - 1] == ' ' and a[i + 1] == '#':
                    a2[i] = '#'
            elif i == len(a) - 1:
                if a[i - 1] == '#' and a[0] == '#':
                    a2[i] = ' '
                elif a[i - 1] == ' ' and a[0] == ' ':
                    a2[i] = ' '
                elif a[i - 1] == '#' and a[0] == ' ':
                    a2[i] = '#'
                elif a[i - 1] == ' ' and a[0] == '#':
                    a2[i] = '#'
        print(str(j + 1) + ')' + ''.join(a2))
        for i in range(len(a2)):
            a[i] = a2[i]
    print('Хотите продолжить играть?')
    print('1) да')
    print('2) нет')
    print('Введите циферку')
    c = input()
print('До встречи! (для выхода из игры введите любой символ)')
input()
