##########################################################################################
# Names: John Wolz, Joseph Ham, Kaelyn Nguyen
# Date: May, 1, 2017
# Descpription: Program that will be on central pi, will be where passwords are entered.
##########################################################################################
from Tkinter import *
import RPi.GPIO as GPIO


class App(Frame):

    # constructor for the window
    def __init__(self, master):
        Frame.__init__(self, master)

        # creates blank space at top
        boarderTop = Label(window)
        boarderTop.pack(expand=1, fill=Y)

        # creates text box
        text = Label(window, text="Please enter password below.")
        text.pack(fill=X)

        # creates blank space to the left
        boarderLeft = Label(window)
        boarderLeft.pack(side=LEFT, expand=1, fill=Y)

        # creates user input box
        global entry
        entry = Entry(window)
        entry.pack(side=LEFT, expand=1, fill=X)

        # creates button, calls the self.checkinput fucntion when pushed
        button = Button(master, text="Enter", command=self.checkinput)
        button.pack(side=LEFT, expand=1)

        # creates blank space to the right
        boarderRight = Label(window)
        boarderRight.pack(side=LEFT, expand=1, fill=Y)

        # creates blank space at the bottom
        boarderBottom = Label(window)
        boarderBottom.pack(expand=1, fill=Y)
        

    def checkinput(self):

        # retrieves the input from the "entry" input box
        i = entry.get()

        # checks the input to determine appropriate response
        if (i == "Z7fme0"):
            print "Password Correct. Left Team Wins!"
        elif (i == "4gPu7v"):
            print "Password Correct. Right Team Wins!"
        else:
            # if password is wrong, the program locks until button is pressed
            print "Incorrect Password. Screen Locked until next attempt."
            window.quit()
                
##################################################################
WIDTH = 410
HEIGHT = 420
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Access Window")
app = App(window)

# sets up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.OUT)

GPIO.output(6, False)

# main program loop
try:
    while True:
        pressed = False
        
        # makes sure button is not already pressed
        while (pressed == False):
            # has LED off
            GPIO.output(6, False)
            
            # checks if button is pressed
            if (GPIO.input(25) == True):
                # turns on LED, runs window main loop, then resumes
                # the "while True" loop
                GPIO.output(6, True)
                pressed = True
                window.mainloop()

# cleans GPIO pins if there is a Keyboard interrupt                
except KeyboardInterrupt:
    GPIO.cleanup()





