txt = []
with open('C:/Test Space of Python/test.txt', 'r') as inf: #Считываем документ
    for line in inf:
        text = list(line.strip().split(' ')) #Вводим строку в переменную text
        max_str = {} #Создаем словарь
        for i in range(len(text)):
            if str.lower(text[i]) in max_str:
                max_str[str.lower(text[i])] += 1 #Если значение строки уже есть в ключе словаря, то увеличиваем значение на один
            else:
                max_str[str.lower(text[i])] = 1 #Если значения строки нет в словаре, то создаем ключ со значением равным единице
        txt.append(max_str) #Добавляем словарь в список

with open('C:/Test Space of Python/out.txt', 'w') as ouf:
    values, key = 0, ' '
    for i in range(len(txt)): #Создаем цикл длинною в список
        max_str = txt[i] #В переменную max_str поочередно передаем словарь из списка
        for k, v in max_str.items(): #Передаем значение и ключ из словаря
            if values < v:  #В данном блоке определяем самое больше значение и его ключ
                values = v
                key = k
        ouf.write(f'{key} {values}\n') #Выводим строку в файл
        ouf.write(f'{max_str}\n')
        values, key = 0, ' ' #Обнуляем переменные для сравнения
