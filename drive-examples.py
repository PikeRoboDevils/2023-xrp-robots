from XRPLib.defaults import *
import time

"""
    By the end of this file students will learn how to control the drivetrain,
    both by setting effort values directly to the motors and by using go_straight and go_turn
"""

# drive straight for a set time period (defualt 1 second)
def drive_straight(drive_time: float = 1):
    drivetrain.set_effort(0.8, 0.8)
    time.sleep(drive_time)
    drivetrain.stop()
    
#end of function
    return

# drive at a slight counter clockwise arc for a set time period (default 1 second)
def arc_turn(turn_time: float = 1):
    drivetrain.set_effort(0.5, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()
    
#end of function
    return

# turn CCW at a point for a set time period (default 1 second)
def point_turn(turn_time: float = 1):
    drivetrain.set_effort(-0.8, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()
    
#end of function
    return

# pivot turn around the left wheel for a set time period (default 1 second)
def swing_turn(turn_time: float = 1):
    drivetrain.set_effort(0, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()
    
#end of function
    return

# Driving in a circle by setting a difference in motor efforts
def circle():
    while True:
        drivetrain.set_effort(0.8, 1)
    
#end of function
    return

# Follow the perimeter of a square with variable sidelength
def square(sidelength):
    for sides in range(4):
        drivetrain.straight(sidelength, 0.8)
        drivetrain.turn(90)
    # Alternatively:
    # polygon(sidelength, 4)
        
#end of function
    return


# Follow the perimeter of an arbitrary polygon with variable side length and number of sides
# Side length in centimeters
def polygon(side_length, number_of_sides):
    for s in range(number_of_sides):
        drivetrain.straight(side_length)
        drivetrain.turn(360/number_of_sides)
        
#end of function
    return

def blink_and_wait():
# blink and wait for user button

    # get setup, warn with flshing LED
    
    # Flash LED at 5Hz
    print("Flashing LED")
    board.led_blink(5)
    
    # Wait for user to press button
    print("Press user button to test drive")
    board.wait_for_button()
    
    # Stop blinking LED
    board.led_off()
    

#end of function
    return
    

# A slightly longer example program showing how a robot may follow a simple path
def test_drive():

# start drive test activity
 
    print("Driving forward 25cm")
    drivetrain.straight(25, 0.8)

    time.sleep(1)

    print("turn 90 degrees right")
    drivetrain.turn(90,0.8)

    time.sleep(1)

    print("turn 90 degrees left by setting speed negative")
    drivetrain.turn(90, -0.8)

    time.sleep(1)

    print("drive backwards 25 cm by setting distance negative")
    # There is no difference between setting speed or distance negative, both work
    drivetrain.straight(-25,0.8)
    
#end of function
    return
    
# warn with flshing LED
blink_and_wait()
    
# test drive the functions!   
test_drive()
# warn with flshing LED
blink_and_wait()

polygon(20, 5)
# warn with flshing LED
blink_and_wait()

polygon(100, 5)
blink_and_wait()
