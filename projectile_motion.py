from __future__ import division
from visual import *
'''
Brendan Hart
 
Projectile Motion
 
9/30/13
'''
 
#define variables
 
ag = -9.8
# gravity
t0 = 0
# time
dt0 = 0.01
# change in time
t1 = 0
# second clock
dt1 = 0.01
# second change in time
 
ivelocity = float(raw_input("What is the intial velocity (m/s): "))
# demand user input for initial velocity
while ivelocity < 0:
    print'Give another value for the initial velocity'
    ivelocity = float(raw_input("What is the intial velocity (m/s): "))
    # check to see if valid velocity
 
angle = float(raw_input("What is the angle to launch the projectile (degrees): "))
while angle > 90 or angle < 0:
    print'Doh! The projectile is not supposed to go off that side of the cliff'
    angle = int(raw_input("What is the angle to launch the projectile: "))
    # check to see if valid angle
 
angle = math.radians(angle)
# convert degrees to radians
 
ivelocityx = ivelocity*math.cos(angle)
print'The initial x velocity is: ', ivelocityx
# inital x velocity in w/ angle radians
ivelocityy = ivelocity*math.sin(angle)
print'The initial y velocity is: ', ivelocityy
# intial y velocity in y/angle radians
 
def ballislife():
    trail = raw_input('Do you want a trail (Yes/No): ')
    if trail.upper() == 'Y' or 'YES':
        trail = True
        return trail
    elif trail.upper() == 'N' or 'NO':
        trail = False
        return trail
    else:
        print'Really! You did not enter the proper input (Yes or No)'
        ballislife()
    # make trail optional 
 
tt = ballislife()
#call the function and assign return value to a variable 
 
projectile = sphere(pos=(0,52.5,0), radius=2.5, make_trail = tt, material = materials.blazed)
cliff = box(pos=(0,25,0), length=20, height=50, width=25, material = materials.shiny)
earth = box(pos=(0,-2.5,0), length=30, height=5, width=25, material = materials.earth)
# e.length is depdent on ivelocity and velcoity of ball
# e.xposition depdent on length
 
 
while true:
    rate(100)
    if projectile.pos.x <= 7.5:
        t0 = t0 + dt0
        l = ivelocityx*t0
        projectile.pos= vector(l, 52.5, 0)
        #Ball rolls on the cliff
    else:
        t1 = t1 + dt1
        # increment time
        h = 52.5 + ivelocityy*t1 + 0.5*ag*t1**2
        # height position of ball
        l = 10 + ivelocityx*t1
        # x position of the ball 
        fvelocityy = ivelocityy + t1*ag
        projectile.pos = vector(l,h,0)
        earth.pos = vector(l,-2.5,0)
        fvelocity = math.sqrt(((fvelocityy - ivelocityy)**2) + (ivelocityx**2))
        if h <= 2.5:
            print'The final velocity is: ', fvelocity
            print'The final y velocity is: ', fvelocityy
            print'The final x velocity is: ', ivelocityx
            print'The time the projectile traveled: ', t1, 's'
            print'The distance the ball is from the cliff is: ', l - 7.5, 'm'
            break
        # projectile motion
