import random

while True:
    try:
        chislo = int(input ("Сколько всего вариантов? "))
        break
    except(TypeError, ValueError):
        print ("Введите целое число")
        continue

while True:
    try:
        variant = int(input ('Сколько из них Вы хотите выбрать? '))
        break
    except(TypeError, ValueError):
        print ("Введите целое число")
        continue
"""сделаем счётчик выбранных вариантов из всего массива
и массив с выбранными вариантами""" 
counter=0
spisok_ans = []
while counter < variant:
    answer = random.randrange(1, chislo)
    if answer not in spisok_ans:
        counter = counter + 1
        spisok_ans.append(answer)
    else:
        continue
spisok_ans.sort()
print ("Из ", chislo," было выбрано ", variant," вариантов: ", spisok_ans)
