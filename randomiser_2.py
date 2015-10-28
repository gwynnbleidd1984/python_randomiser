import random

while True:
    try:
        chislo = int(input ("Input please the quantity of options: "))
        break
    except(TypeError, ValueError):
        print ("This is not an integer. Please input an integer")
        continue

while True:
    try:
        variant = int(input ('Input please the quantity of chosen options: '))
        if variant>chislo:
            print("You have chosen too much options." "\nPlease try again")
            continue
        break
    except(TypeError, ValueError):
        print ("This is not an integer. Please input an integer")
        continue

counter = 0
spisok_ans = []
while counter < variant:
    answer = random.randrange(1, chislo+1)
    if answer not in spisok_ans:
        counter += 1
        spisok_ans.append(answer)
    else:
        continue
spisok_ans.sort()

print ("\nYou have chosen " , variant," options from", chislo, ". \nHere is the list: ", spisok_ans)
input("\n\nPress the enter key to exit.")
