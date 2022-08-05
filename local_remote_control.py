import XInput
import time
import serial as ser


controllers = XInput.get_connected()
print(controllers)
CONTROLLER = controllers.index(True)
print(CONTROLLER)
ser_front = ser.Serial(port='COM4',baudrate=115200)
ser_back = ser.Serial(port='COM5',baudrate=115200)


def read_response(stick_msg):
    msg_int = [round(num,0) for num in stick_msg]
    if msg_int == [0,0]: # STOP
        command_right_front = "!S 1 0000" + "\r"
        command_left_front = "!S 2 0000" + "\r"
        command_right_back = "!S 1 0000" + "\r"
        command_left_back = "!S 2 0000" + "\r"

    elif msg_int == [1,0]: # FORWARD
        command_right_front = "!S 2 075" + "\r"
        command_left_front =  "!S 1 -075" + "\r"
        command_right_back = "!S 2 -075" + "\r"
        command_left_back = "!S 1 075" + "\r"

    elif msg_int == [-1,0]: # BACKWARD
        command_right_front = "!S 2 -075" + "\r"
        command_left_front =  "!S 1 075" + "\r"
        command_right_back = "!S 2 075" + "\r"
        command_left_back = "!S 1 -075" + "\r"

    elif msg_int == [0,1]: # RIGHT
        command_right_front = "!S 2 -075" + "\r"
        command_left_front =  "!S 1 -075" + "\r"
        command_right_back = "!S 2 075" + "\r"
        command_left_back = "!S 1 075" + "\r"

    elif msg_int == [1,1]: # FORWARD RIGHT 
        command_right_front = "!S 2 0000" + "\r"
        command_left_front =  "!S 1 -075" + "\r"
        command_right_back = "!S 2 0000" + "\r"
        command_left_back = "!S 1 075" + "\r"

    elif msg_int == [-1,1]: # BACKWARD RIGHT 
        command_right_front = "!S 2 0000" + "\r"
        command_left_front =  "!S 1 075" + "\r"
        command_right_back = "!S 2 0000" + "\r"
        command_left_back = "!S 1 -075" + "\r"

    elif msg_int == [0,-1]: # LEFT 
        command_right_front = "!S 2 075" + "\r"
        command_left_front =  "!S 1 075" + "\r"
        command_right_back = "!S 2 -075" + "\r"
        command_left_back = "!S 1 -075" + "\r"

    elif msg_int == [1,-1]: # FORWARD LEFT
        command_right_front = "!S 2 075" + "\r"
        command_left_front =  "!S 1 0000" + "\r"
        command_right_back = "!S 2 -075" + "\r"
        command_left_back = "!S 1 0000" + "\r"

    elif msg_int == [-1,-1]: # BACKWARD LEFT
        command_right_front = "!S 2 -075" + "\r"
        command_left_front =  "!S 1 0000" + "\r"
        command_right_back = "!S 2 075" + "\r"
        command_left_back = "!S 1 0000" + "\r"


    ser_front.write(command_right_front.encode())
    print(command_right_front.encode())
    ser_back.write(command_right_back.encode())
    ser_front.write(command_left_front.encode())
    ser_back.write(command_left_back.encode())


while(True):

    input_state = XInput.get_state(CONTROLLER)
    stick = XInput.get_thumb_values(input_state)
    stick_lst = [stick[0][0],stick[0][1],stick[1][0],stick[1][1]]
    stick_msg = [round(stick[0][1],4), round(stick[1][0],4)]
    read_response(stick_msg)
    time.sleep(0.1)

    