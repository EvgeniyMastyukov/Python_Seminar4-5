# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


with open('input.txt', 'r') as file:
    lst = file.readline()

    lst = list(map(int, lst.split(' ')))

    for i in range(len(lst)):
        if ((lst[i] - 1) != lst[i - 1]) and (i != 0):
            print(f'Недостающий элемент = {lst[i] - 1}')
