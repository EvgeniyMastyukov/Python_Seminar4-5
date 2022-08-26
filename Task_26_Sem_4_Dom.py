# На вход поступает список из целых чисел и отдельно число target. 
# Нужно найти индексы таких двух чисел из списка, которые в сумме равны target.
# Пример: Для [2, 7, 11, 13] и target=9 => [0, 1]

users_list = [17, 10, -1, 0, 3, 9]                 #[2, 7, 11, 13]
target = 9
for i in range(len(users_list)- 1):
    for j in range(i + 1, len(users_list)):
        if users_list[i] + users_list[j] == target:
            print('[' + str(i) + ',' + str(j) + ']')

