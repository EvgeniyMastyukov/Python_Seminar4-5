# Создайте программу для игры в ""Крестики-нолики"".

field = '1-|2-|3-\n4-|5-|6-\n7-|8-|9-'

user1 = field.replace('2', 'x')  #'\n ------')
print(user1,'\n =====')

user2 = user1.replace('4', '0')
print(user2,'\n =====')

