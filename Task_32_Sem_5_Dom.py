# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = 'Давно выясабвнено, что при оценкеабв дизайна и композициабви читаемый текст мешает сосредоточиться.' 
def remove (text):
    list_text = text.split(' ')
    #print(list_text)
    new_list_text = []
    for el in list_text:
        if el.find('абв') == -1:
            new_list_text.append(el)
    string = ' '.join(new_list_text)    
    return string
    
result = remove(text)
print(result)





