import time
import socket
import RPi.GPIO as GPIO
import board
import adafruit_mpu6050

#i2c = board.I2C()
#mpu = adafruit_mpu6050.MPU6050(i2c)
integrationPosY = 0
orientation = "up"

#Sets pins for finger magnet switches
GPIO.setmode(GPIO.BCM)

#White/Middle Finger
GPIO.setup(12, GPIO.IN)

#Orange/Index Finger
GPIO.setup(16, GPIO.IN)

#Blue/Ring Finger
GPIO.setup(20, GPIO.IN)

#Yellow/Pinky Finger
GPIO.setup(21, GPIO.IN)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's IP and port
sock.connect(('192.168.1.10', 12345))


#Main polling loop
while True:
    #Calculates orientation of the glove
    gyroY = mpu.gyro[1]
    integrationPosY = integrationPosY + gyroY

    if integrationPosY > -45 and integrationPosY < 45:
        orientation = "up"
    if integrationPosY > 45 and integrationPosY < 135:
        orientation = "right"
    if integrationPosY > 135 and integrationPosY < 225:
        orientation = "down"
    if integrationPosY > -135 and integrationPosY < -45:
        orientation = "left"

    if orientation == "up":
        if GPIO.input(16) == 0:
            sock.sendall(b'left_click_down')
            while True:
                if GPIO.input(16) == 1:
                    sock.sendall(b'left_click_up')
                    break

        if GPIO.input(12) == 0:
            sock.sendall(b'right_click_down')
            while True:
                if GPIO.input(12) == 1:
                    sock.sendall(b'right_click_up')
                    break

        if GPIO.input(20) == 0:
            sock.sendall(b'alt_tab_down')
            while True:
                if GPIO.input(20) == 1:
                    sock.sendall(b'alt_tab_up')
                    break

        if GPIO.input(21) == 0:
            sock.sendall(b'enter_down')
            while True:
                if GPIO.input(21) == 1:
                    sock.sendall(b'enter_up')
                    break
    

    if orientation == "right":
        if GPIO.input(16) == 0:
            sock.sendall(b'ctrl_c_down')
            while True:
                if GPIO.input(16) == 1:
                    sock.sendall(b'ctrl_c_up')
                    break

        if GPIO.input(12) == 0:
            sock.sendall(b'ctrl_v_down')
            while True:
                if GPIO.input(12) == 1:
                    sock.sendall(b'ctrl_v_up')
                    break

        if GPIO.input(20) == 0:
            sock.sendall(b'alt_tab+_down')
            integrationPosZ = 0
            while True:
                gyroZ = mpu.gyro[2]
                integrationPosZ = integrationPosZ + gyroZ
                if integrationPosZ < 0:
                    sock.sendall(b'left_arrow')
                elif integrationPosZ > 0:
                    sock.sendall(b'right_arrow')
                if GPIO.input(20) == 1:
                    sock.sendall(b'alt_tab+_up')
                    break

        if GPIO.input(21) == 0:
            sock.sendall(b'ctrl_x_down')
            while True:
                if GPIO.input(21) == 1:
                    sock.sendall(b'ctrl_x_up')
                    break
    
    if orientation == "down":
        if GPIO.input(16) == 0:
            sock.sendall(b'ctrl_s_down')
            while True:
                if GPIO.input(16) == 1:
                    sock.sendall(b'ctrl_s_up')
                    break

        if GPIO.input(12) == 0:
            sock.sendall(b'ctrl_z_down')
            while True:
                if GPIO.input(12) == 1:
                    sock.sendall(b'ctrl_z_up')
                    break

        if GPIO.input(20) == 0:
            sock.sendall(b'ctrl_y_down')
            while True:
                if GPIO.input(20) == 1:
                    sock.sendall(b'ctrl_y_up')
                    break

        if GPIO.input(21) == 0:
            sock.sendall(b'esc_down')
            while True:
                if GPIO.input(21) == 1:
                    sock.sendall(b'esc_up')
                    break
        


sock.close()