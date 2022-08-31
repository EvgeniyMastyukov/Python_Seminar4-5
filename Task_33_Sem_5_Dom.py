#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
string = 'FFFFGGGBBBBAAV'   #=> 4F3G4B2A1V

new_str = ''
count = 1
for i in range(1,len(string)):
    if string[i] == string[i-1]: 
        count += 1
        
    elif string[i] != string[i-1]:
        new_str += str(count) + string[i-1]
        count = 1
new_str += str(count) + string[-1]    

print(new_str)

