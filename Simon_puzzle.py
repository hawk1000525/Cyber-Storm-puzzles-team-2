########################################
# Name: Joseph Ham
# Date: 2/17/17
# Description: Simon
########################################
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

# set to True to enable debugging output
DEBUG = False

# initialize the pygame library
pygame.init()

# set the GPIO pin numbers
# the switches (from L to R)
switches = [ 23, 18, 24, 25 ]
# the LEDs (from L to R)
leds = [4, 17, 22, 5 ]
# the sounds that map to each LED (from L to R)
sounds = [ pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav") ]
start = [ 0, 1, 2, 3 ]

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

# this function turns the LEDs on
def all_on():
        for i in leds:
                GPIO.output(leds, True)

# this function turns the LEDs off
def all_off():
        for i in leds:
                GPIO.output(leds, False)

# this functions flashes the LEDs a few times when the player loses the game
def lose():
        for i in range(0, 4):
                all_on()
                sleep(0.5)
                all_off()
                sleep(0.5)

def new():
        # each item in the sequence represents an LED (or switch), indexed at 0 through 3
        seqbuilder = 0
        new.seq = []
        while seqbuilder < 6:
                new.seq.append(randint(0,3))
                seqbuilder += 1

def playseq():
# display the sequence using the LEDs
        for s in new.seq:
        # randomly pick output method
                display = randint(0, 2)
                if (DEBUG):
                        pass
                if (display == 0):
                        GPIO.output(leds[s], True)
                        # wait and turn the LED off again
                        sleep(0.9)
                        GPIO.output(leds[s], False)
                        sleep(0.4)
                elif (display == 1):
                        print s
                        sleep(1.3)
                else:
                        # play its corresponding sound
                        sounds[s].play()
                        sleep(1.3)

# the main part of the program

print "Welcome to the first puzzle."
sleep(1.0)
print "Try to play the sequence back by pressing the switches."
sleep(1.0)

# initialize the count of switches pressed to 0
count = 0
incorrect = 0
correct = 0

# we'll discuss this later, but this allows us to detect
# when Ctrl+C is pressed so that we can reset the GPIO pins

# keep going until the user presses
while (correct != 2):
        print "Watch the screen and LEDs and listen to the sound."
        for s in start:
                GPIO.output(leds[s], True)
                print s
                sounds[s].play()
                # wait and turn the LED off again
                sleep(0.9)
                GPIO.output(leds[s], False)
                sleep(0.4)
        print "Here is the first sequence."
        while (correct < 3):
                new()
                count = 0
                if (DEBUG):
                        # display the sequence to the console
                        print new.seq
                playseq()

                                        # wait for player input (via the switches)
                print "Now play it back."
                # keep accepting player input until the number of items in the sequence is reached
                while (count < len(new.seq)):
                        # initially note that no switch is pressed
                        # this will help with switch debouncing
                        pressed = False
                        # so long as no switch is currently pressed...
                        while (not pressed):
                                # ...we can check the status of each switch
                                for i in range(len(switches)):
                                        # if one switch is pressed
                                        while (GPIO.input(switches[i]) == True):
                                                # note its index
                                                val = i
                                                # note that a switch has now been pressed
                                                # so that we don't detect any more switch presses
                                                pressed = True

                        # light the matching LED
                        GPIO.output(leds[val], True)
                        print val
                        # play its corresponding sound
                        sounds[val].play()
                        # wait and turn the LED off again
                        sleep(1)
                        GPIO.output(leds[val], False)
                        sleep(0.25)

                        # check to see if this LED is correct in the sequence
                        if (val != new.seq[count]):
                                # player is incorrect; invoke the lose function
                                lose()
                                if (incorrect < 2):
                                        print "Incorrect. Try again."
                                        incorrect += 1
                                        count = -1
                                        sleep(1.5)
                                        print "Here is the set again. It might look a bit different."
                                        sleep(1.5)
                                        playseq()
                                        print "Now play it back."
                                else:
                                        print "Incorrect. Maximum attempts expired. Generating new sequence."
                                        incorrect = 0
                                        new()
                                        count = -1
                                        break
                        count += 1

                        if (correct == 2 and count == 6):
                                print "Congratulations!"
                                GPIO.cleanup()
                                sleep (2.0)
                                # exit the game
                                raise SystemExit
                        elif (correct <= 3 and count == 6):
                                print "Congratulations. Next one."
                                correct += 1
                                incorrect = 0
                                sleep (2.0)
                                count = 0
                                break
