number = int(input('Введите число: '))

for i in range(1, number):
    for j in range(i+1, number):
        if number % (i+j) == 0:
            print (i, j, sep='', end='')



