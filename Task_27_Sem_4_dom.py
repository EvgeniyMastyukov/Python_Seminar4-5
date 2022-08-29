# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

text = '2 1 4 5 5 3 0 7 9 1'
new_text = list(map(int,text.split(' ')))

print(new_text)
print(f'min number = {min(new_text)}')  
print(f'max number = {max(new_text)}') 