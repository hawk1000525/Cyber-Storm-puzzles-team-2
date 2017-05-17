from time import sleep

print "Welcome team."
sleep (2.0)
print "Your mission: hack into the central computer before your rivals."
sleep (2.0)
print "Here is your first challenge. Time begins now."
sleep(2.0)
print"_________________________________________________"

try:
    execfile('Simon_puzzle.py')
except SystemExit:
    print "Here is part of the password:"

sleep (2.0)
print "4gP"
sleep (2.0)
print "Here is the next challenge."
sleep(2.0)

try:
    execfile("greater_math.py")
except SystemExit:
    print "Here is the rest of the password:"
    
sleep (2.0)
print "u7v"
sleep(2.0)
print "Go enter your password."
