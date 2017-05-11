from random import randint

def CreateEqu():
    operators = ["+", "-", "*", "/"]
    global equ
    global equa
    equ = [] #equations
    equa = [] #equation answers

    #picks two random numbers and a math function
    for i in range (0,2):
        a = randint(0,21)
        b = operators[randint(0,3)]
        c = randint(1,21)

        #adds the new equation to the list
        equ.append("{} {} {}".format(a,b,c))

        #calculates the answers
        if b == "+":
            equa.append(a + c)
        elif b == "-":
            equa.append(a - c)
        elif b == "*":
            equa.append(a * c)
        elif b == "/":
            equa.append(a / c)

state = True
points = 0

while state == True:
    print "Pick which is greater!"
    CreateEqu()
    print "1) {}".format(equ[0])
    print "2) {}".format(equ[1])
    print "3) Equal"
    print "Points: {}".format(points)

    action = raw_input("Pick 1, 2 or, 3 \n")

    if action == "1":
        if equa[0] > equa[1]:
            points += 1

    if action == "2":
        if equa[1] > equa[0]:
            points += 1

    if action == "3":
        if equa[0] == equa[1]:
            points += 1

    if points == 10:
        state = False
        print "You have won! Here is the next piece of password _____"
