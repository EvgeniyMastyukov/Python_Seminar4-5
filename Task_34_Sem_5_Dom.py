# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
candies = 2021
user1 = 0 # Ход первого игрока
user2 = 0 # Ход второго игрока
user1 = 2021%29 
user1_count = 1
user2_count = 0
while candies >= 0:      
    user2 = random.randint(1,29)  
    candies -= user2
    if candies <= 0: break
    print('2ой', user2_count)
    user1 = 29 - user2 
    candies -= user1
    if candies <= 0: break 
    print('1ый', user1_count)
    user2_count += 1
    user1_count += 1 

print(user1_count)
print(user2_count)    
if  user1_count > user2_count: print('Победил 1-й игрок')
if  user2_count == user1_count: print('Победил 2-й игрок')





