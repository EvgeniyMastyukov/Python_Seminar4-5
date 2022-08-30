# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Пример:    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst =  [1, 5, 2, 3, 4, 6, 1, 7] #[8, 8, 8, 2, 3, 4, 6, 1, 7]
res = []
i = 0
a = max(lst)
print(lst.index(a)) #поиск индекса максим элемента
while(i < len(lst)):    
    if lst[i] < max(lst):
        res.append(lst[i])
        break       
    i+=1          
for i in range(1,len(lst)): 
   if lst[i] > res[len(res)-1] and lst[i] != max(lst):
    res.append(lst[i]) 
         
print(res)