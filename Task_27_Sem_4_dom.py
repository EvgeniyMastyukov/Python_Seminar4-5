# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

text = '2 1 4 5 5 3 0 7 9 1'
new_text = text.split(' ')
for i in range(len(new_text)):
    new_text[i] = int(new_text[i])
print(new_text)
print(f'min number = {min(new_text)}')  
print(f'max number = {max(new_text)}') 