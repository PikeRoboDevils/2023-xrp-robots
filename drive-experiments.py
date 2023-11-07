# Initial code pulled from the installation verification code and API documents
from XRPLib.defaults import *
import time


# Follow the perimeter of a square with variable sidelength
def square(sidelength):
    for sides in range(4):
        drivetrain.straight(sidelength, 0.8)
        drivetrain.turn(90)
    # Alternatively:
    # polygon(sidelength, 4)
    ## end of function / subroutine ##

# Driving in a circle by setting a difference in motor efforts
def circle():
    while True:
        drivetrain.set_effort(0.8, 1) 
    ## end of function / subroutine ##
        
# Follow the perimeter of an arbitrary polygon with variable side length and number of sides
# Side length in centimeters
def polygon(side_length, number_of_sides):
    for s in range(number_of_sides):
        drivetrain.straight(side_length)
        drivetrain.turn(360/number_of_sides)        
    ## end of function / subroutine ##
    
# main fuunction to drive robot around
def ivp():
    
    # blink and and wait for button press
    # Flash LED at 5Hz
    board.led_blink(5)

    board.wait_for_button()

    time.sleep(1)
#    while (rangefinder.distance() > 10): # not quite working the way it was expected!
    while(True):
        square(25)

# move arm
        time.sleep(1)
        servo_one.set_angle(90)
        time.sleep(1)
        servo_one.set_angle(0)
        time.sleep(1)
        servo_one.set_angle(180)
        time.sleep(1)
        
        polygon(25, 5)

# move a bit         
        time.sleep(1)
        drivetrain.straight(25, 1.0)
        time.sleep(1)
        drivetrain.turn(90,0.8)
        time.sleep(1)
        drivetrain.turn(90, -0.8)
        time.sleep(1)
        drivetrain.straight(-25,0.2)        
        time.sleep(1)
                
    ## end of function / subroutine ##

# start of main code body
ivp()
