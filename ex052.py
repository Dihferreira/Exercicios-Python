num = int(input('Digite um número: '))
tot = 0
for c in range(1, num +1):
    if num % c ==0:
        print('\33[31m', end='')
        tot += 1
    else:
        print('\033[37m', end='')
    print('{} '.format(c),end='')
print('\n\033[mO {} foi divisivel por {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é primo!!!')
else:print('Por isso nao é primo!!!')
