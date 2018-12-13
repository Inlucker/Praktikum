import queue as q

file = open('input.txt', 'r')

inp = ''
for i in file:
    for j in i:
        if (j != '\n'):
            inp += j
        else:
            inp += ' '
inp += ' '

file.close()

tmp = ''
svNumber = 0
counter = 0
cityCounter = 0
flag = True
for i in inp:
    if (i != ' '):
        tmp += i
    else:
        tmp = int(tmp)
        if (counter == 0):
            mas = [[0 for id1 in range(2)] for id2 in range(tmp)]
            svNumber = tmp
            counter = tmp
        else:
            if (flag):
                mas[svNumber - counter][0] = tmp
                flag = False
            else:
                mas[svNumber - counter][1] = tmp
                flag = True
                counter -= 1
                
        tmp = ''
        
        if (counter == 0):
            
            uzNumber = max(max(i) for i in mas) + 1

            rez = [[0 for id1 in range(uzNumber)] for id2 in range(uzNumber)]

            for i in mas:
                for j in mas:
                    if (i == j[::-1]):
                        rez[i[0]][i[0]] = -1
                        rez[i[1]][i[1]] = -1
                        rez[i[0]][i[1]] = -1
                        rez[i[1]][i[0]] = -1
            
            flag2 = True
            while (flag2):
                flag2 = False
                for i in mas:
                    for j in range(uzNumber):
                        for k in range(uzNumber):
                            if (rez[j][k] == -1 and i[1] == j and rez[i[0]][k] != -1):
                                rez[i[0]][k] = -1
                                flag2 =True
                            
                            if (rez[i[0]][i[0]] == -1 and i[0] == j and i[1] == k and rez[j][k] != -1):
                                rez[j][k] = -1
                                flag2 =True
            
            for k in range(uzNumber):
                frontier = q.Queue()
                frontier.put(k)

                while (not frontier.empty()):
                    current = frontier.get()
                     
                    for i in range (len(mas)):
                        if (mas[i][0] == current):
                            if (rez[k][mas[i][1]] != -1):
                                frontier.put(mas[i][1])
                                rez[k][mas[i][1]] += 1
                 
            print('matrix for city', cityCounter)
            for i in rez:
                for j in i:
                    print(j, end = ' ')
                print()
            print()

            cityCounter += 1
            mas = []
