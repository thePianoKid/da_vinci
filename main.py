#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import math

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Please note that one full corkscrew rotation of the robot is 1.8 rotations

brick = EV3Brick()
WHEEL_DI = 4.32  # in centimeters

# Initialize ports
A = Motor(Port.A)
B = Motor(Port.B)
C = Motor(Port.C)
touch_sensor = TouchSensor(Port.S1)
gyro_sensor = GyroSensor(Port.S2)


def engage():
    A = Motor(Port.A)
    B = Motor(Port.B)
    C = Motor(Port.C)
    touch_sensor = TouchSensor(Port.S1)
    gyro_sensor = GyroSensor(Port.S2)
    while(touch_sensor.pressed() == False):
        time.sleep(0.01)
    time.sleep(1)


def tankMove(motor1, motor2, speed1, speed2, degm1, degm2):
    A = Motor(Port.A)
    B = Motor(Port.B)
    C = Motor(Port.C)
    '''
    motor1: port to initialize (e.g. Motor(Port.A))
    motor2: another port to initialize (e.g. Motor(Port.B))
    speed: speed of both motors (max: 1000)
    degm1: # of degrees motor1 must turn (if positive, then clockwise, if negative, then counterclockwise)
    degm2: # of degrees motor2 must turn (if positive, then clockwise, if negative, then counterclockwise)
    '''

    motor1.run_target(speed1, degm1, Stop.BRAKE,
                      False)  # run_angle(speed, rotation_angle, stop_type=Stop.COAST, wait=True)
    motor2.run_target(speed2, degm2, Stop.BRAKE)


def tankMoveRot(motor1, motor2, speed1, speed2, rotm1, rotm2):
    B = Motor(Port.B)
    C = Motor(Port.C)
    '''
    motor1: port to initialize (e.g. Motor(Port.A))
    motor2: another port to initialize (e.g. Motor(Port.B))
    speed: speed of both motors (max: 1000)
    rotm1: # of rotations motor1 must turn (if positive, then clockwise, if negative, then counterclockwise)
    rotm2: # of rotations motor2 must turn (if positive, then clockwise, if negative, then counterclockwise)
    '''

    # run_angle(speed, rotation_angle, stop_type=Stop.COAST, wait=True)
    motor1.run_target(speed1, (rotm1*360), Stop.BRAKE, False)
    motor2.run_target(speed2, (rotm2*360), Stop.BRAKE)


def tankMoveLen(motor1, motor2, speed1, speed2, dist):
    B = Motor(Port.B)
    C = Motor(Port.C)

    num_of_rot = dist/(WHEEL_DI*math.pi)
    print(num_of_rot)
    tankMoveRot(motor1, motor2, speed1, speed2, num_of_rot, num_of_rot)


def medMotor(port, speed, deg):
    A = Motor(Port.A)
    # -0.5 rotations will lift the marker up, the process is invertable
    '''
    port: port to initialize (e.g. Motor(Port.A))
    speed: speed of motor (max: 1000)
    deg: # of degrees motor1 must turn (if positive, then clockwise, if negative, then counterclockwise)
    '''
    port.run_target(speed, deg, Stop.BRAKE)


def gyroTurn(deg, speed):
    B = Motor(Port.B)
    C = Motor(Port.C)
    gyro_sensor = GyroSensor(Port.S2)

    # reset the gyro angle to 0
    gyro_sensor.angle()
    time.sleep(0.5)
    while(gyro_sensor.angle() != 0):
        time.sleep(0.1)

    while deg != gyro_sensor.angle():
        if deg > 0:
            B.run(-1*speed)
            C.run(speed)
        else:
            B.run(speed)
            C.run(-1*speed)
    B.brake()
    C.brake()


def penUp():
    A = Motor(Port.A)
    medMotor(A, 500, -180)


def penDown():
    A = Motor(Port.A)
    medMotor(A, 500, 180)


def centerDome():
    # See https://docs.google.com/document/d/136q1P2ljUweMYeG0JeVoWiPpX8D0Bm5wqXMY0N2BvJM/edit for information on this funciton
    penDown()
    tankMoveRot(B, C, 500, 45, 2.27, 0.222)
    tankMoveRot(B, C, 135, 500, 0.225, 0.833)
    penUp()
    tankMoveRot(B, C, 100, 100, -0.3, 0.3)
    penDown()
    tankMoveRot(B, C, 100, 100, 0.2, 0.2)
    penUp()
    tankMoveRot(B, C, 100, 100, -0.2, -0.2)
    tankMoveRot(B, C, 100, 100, -0.3, 0.3)
    penDown()
    tankMoveRot(B, C, 500, 135, -0.833, -0.225)
    tankMoveRot(B, C, 45, 500, -0.222, -2.27)
    penUp()


turn_speed = 25

'''
engage()
gyroTurn(42, turn_speed)
centerDome()
gyroTurn(133, turn_speed)
Motor(Port.A).brake()
tankMoveLen(B, C, 100, 100, -0.5)
penDown()
tankMoveLen(B, C, 100, 100, 15.5)
penUp()
gyroTurn(88, turn_speed)
penDown()
tankMoveLen(B, C, 100, 100, 1)
penUp()
gyroTurn(88, turn_speed
'''

engage()
penDown()
tankMoveLen(B, C, 100, 100, 15.5)
penUp()
gyroTurn(89, turn_speed)
penDown()
tankMoveLen(B, C, 100, 100, 23)
penUp()
gyroTurn(89, turn_speed)
penDown()
tankMoveLen(B, C, 100, 100, 4.25)
penUp()
gyroTurn(89, turn_speed)
penDown()
tankMoveLen(B, C, 100, 100, 17)
penUp()
gyroTurn(-89, turn_speed)
penDown()
tankMoveLen(B, C, 100, 100, 8)
penUp()
