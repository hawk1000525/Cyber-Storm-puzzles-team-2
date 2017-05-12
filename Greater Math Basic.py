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

# Main loop of the puzzle
while state == True:
    print "Pick which is greater! Go for 10 points!"
    CreateEqu()
    print "1) {}".format(equ[0])
    print "2) {}".format(equ[1])
    print "3) Equal"
    print "Points: {}".format(points)

    action = raw_input("Pick 1, 2 or, 3 \n")

    if action == "1":
        # checks if answer is correct
        if equa[0] > equa[1]:
            points += 1

    if action == "2":
        # checks if answer is correct
        if equa[1] > equa[0]:
            points += 1

    if action == "3":
        # checks if answer is correct
        if equa[0] == equa[1]:
            points += 1

    # puzzle ends once player gets 10 correct answers
    if points == 10:
        state = False
        print "You have won! Here is the next piece of password 'me0'"
