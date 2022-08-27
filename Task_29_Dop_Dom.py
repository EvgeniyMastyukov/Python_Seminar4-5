# Итак, чтобы решить полное квадратное уравнение, надо вычислить дискриминант D. D = b ^2 – 4ас. 
# В зависимости от того какое значение имеет дискриминант, мы и запишем ответ. 
# Если дискриминант отрицательное число (D < 0), то корней нет. 
# Если же дискриминант равен нулю, то х = (-b)/2a. 
# Когда дискриминант положительное число (D > 0), тогда х 1 = (-b - √D)/2a, и х 2 = (-b + √D)/2a.

import math
user_list = []
for i in range(3):
    string = 'Введите значение коэффициента №' + str(i+1) + ': '
    user_list.append(int(input(string)))
print(user_list)
a = user_list[0]
b = user_list[1]
c = user_list[2]
x = None
x1 = None
x2 = None
# expression = a*x**2 + b*x + c == 0
discrim = b**2 - 4*a*c
if discrim > 0:
    x1 = (-b - math.sqrt(discrim)) / (2 * a)
    x2 = (-b + math.sqrt(discrim)) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif discrim == 0:
    x = (-b)/(2*a)
    print(f'Один корень = {x}')    
elif discrim < 0:
    print("корней нет")
  
print(discrim) 


