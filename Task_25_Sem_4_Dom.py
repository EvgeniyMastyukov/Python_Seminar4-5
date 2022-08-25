# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные
# числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 2-х самых часто встречаемых чисел.

words = '1,2,3,4,3,3,0,2,7,8'
text = words.split(",")
print(text)
for i in range(len(text)):
    text[i] = int(text[i])

num_dictionary = {}
text.sort()
keys_dic = []
for i in text:
    keys_dic.append(i)

for el in keys_dic:
    if keys_dic.count(el) > 1:
        while keys_dic.count(el) > 1:
            keys_dic.remove(el)

value_dic = []
for i in keys_dic:
    value_dic.append(text.count(i))    

num_dictionary = {}
index = 0
for el in keys_dic:
    num_dictionary[el] = value_dic[index]
    index += 1
    
max1 = 0
max2 = 0
for i in num_dictionary:
    if num_dictionary[i] > max1:
        max1 = num_dictionary[i]
    if num_dictionary[i] > max2 and max2 < max1:
        max2 = num_dictionary[i]    
print(max1, max2)    
new_dictionary = {}
for i in num_dictionary:
    if num_dictionary[i] == max1 or num_dictionary[i] == max2:
        new_dictionary[i] = num_dictionary[i]  

     
print(text)
print(keys_dic)
print(value_dic)
print(num_dictionary)
print(num_dictionary.items())
print()
print(new_dictionary) 



# num_dictionary = \
#     {
#         1: 1,
#         2: 2,
#         3: 3,
#         4: 1,
#         7: 1,
#         8: 1
#     }
# print(num_dictionary)
# def count_it(sequence):