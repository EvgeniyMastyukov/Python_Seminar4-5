# Вы получаете на вход число N. Требуется проверить, является ли оно степенью числа 4, 
#т.е. существует такой x, что 4^x = N
# Пример: N=16 => True; N=5 => False


num =  int(input('Введите число N: '))

while num > 1:
   num = num/4
   if num == 1:
      print('да')
   else:
      print('нет')

# while num != 1:
#    if num%4 == 0:
#     print('да')
#    else:
#     print('нет')
#     break    
#    num //= 4 


