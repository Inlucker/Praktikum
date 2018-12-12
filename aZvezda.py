import queue as q

mas = [[0, 1], [0, 2], [0, 4], [1, 0], [2, 4], [2, 3], [3, 1], [4, 3]]

rez = [[0 for id1 in range(5)] for id2 in range(5)]

for i in mas:
   for j in mas:
      if (i == j[::-1]):
         for k in range(5):
            rez[i[0]][k] = -1
            rez[i[1]][k] = -1

flag2 = True
while (flag2):
   flag2 = False
   for i in mas:
      for j in range(5):
         if (rez [j][0] == -1 and i[1] == j and rez[i[0]][k] != -1):
            for k in range(5):
               rez[i[0]][k] = -1
            flag2 = True

for i in rez:
   for j in i:
      print(j, end = ' ')
   print()
print()

for k in range(5):
   if (rez[k][0] != -1):
      frontier = q.Queue()
      frontier.put(k)

      while (not frontier.empty()):
         current = frontier.get()
         #print(current)
         
         for i in range (len(mas)):
               if (mas[i][0] == current):
                  frontier.put(mas[i][1])
                  rez[k][mas[i][1]] += 1

for i in rez:
   for j in i:
      print(j, end = ' ')
   print()

