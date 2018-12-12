#import os
import queue as q

#Считываем ввод
file = open('input.txt', 'r')

inp = ''
for i in file:
    for j in i:
        if (j != '\n'):
            inp += j
        else:
            inp += ' '
inp += ' '
#print(inp)

#Записываем все пути в двумерный массив
tmp = '' #Переменная для хранения текущего числа из ввода
svNumber = 0 #Число связей между узлами (число улиц в городе)
counter = 0 #Cчётчик улиц оставшихся для определения
cityCounter = 0 #Счётчик гродов
flag = True #Флаг отвечающий за отличии того что мы считываем (номер начального/конечного узла)
for i in inp:
    if (i != ' '):
        tmp += i
    else:
        tmp = int(tmp)
        #print(tmp)
        if (counter == 0): #Тот случай когда в tmp лежит кол-во связей
            mas = [[0 for id1 in range(2)] for id2 in range(tmp)]
            svNumber = tmp
            counter = tmp
        else:
            if (flag): #Запись номера начального узла текущей связи
                mas[svNumber - counter][0] = tmp
                flag = False
            else: #Запись номера конечного узла текущей связи
                mas[svNumber - counter][1] = tmp
                flag = True
                counter -= 1
                #print(mas)
        tmp = ''
        
        if (counter == 0):
            #print(mas)
            
            uzNumber = max(max(i) for i in mas) + 1 # Считаем колличество узлов
            #print(uzNumber)

            #Находим результат (двумерный массив кол-ва путей)
            rez = [[0 for id1 in range(uzNumber)] for id2 in range(uzNumber)]

            #Заранее заполняем результат минус единицами в нужных местах
            for i in mas:
               for j in mas:
                  if (i == j[::-1]):
                     for k in range(uzNumber):
                        rez[i[0]][k] = -1
                        rez[i[1]][k] = -1
            flag2 = True #Флаг отвечающий за то что мы не закончили начальную обработку результата
            while (flag2):
               flag2 = False
               for i in mas:
                  for j in range(uzNumber):
                     if (rez [j][0] == -1 and i[1] == j and rez[i[0]][k] != -1):
                        for k in range(uzNumber):
                           rez[i[0]][k] = -1
                        flag2 = True

            #Заполняем результат построчно с помощью алгоритма A*
            for k in range(uzNumber):
               if (rez[k][0] != -1): #Проверка на то что из узла k нельзя попасть в цикл
                  frontier = q.Queue() #Создаём очередь типа FIFO для хранения текущих узлов
                  frontier.put(k) #Начинам с узла, номер которого соответствует номеру текущей строки в результате

                  while (not frontier.empty()):
                     current = frontier.get()
                     #print(current)
                     
                     for i in range (len(mas)):
                           if (mas[i][0] == current):
                              frontier.put(mas[i][1]) #Добавляем в очередь соседние узлы
                              rez[k][mas[i][1]] += 1 #Считаем результат

            #Выводим результат                  
            print('matrix for city', cityCounter)
            for i in rez:
               for j in i:
                  print(j, end = ' ')
               print()
            print()

            cityCounter += 1
            mas = []
    
#os.system('PAUSE')
