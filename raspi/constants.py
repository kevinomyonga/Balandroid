"""
File containing all the constants used in the different files
"""

# PS4 Controller Button Numbering
SQUARE              = 0
X                   = 1
CIRCLE              = 2
TRIANGLE            = 3
L1                  = 4
R1                  = 5
L2                  = 6
R2                  = 7
SHARE               = 8
OPTIONS             = 9
L3 					= 10
R3 					= 11
PS4_ON_BUTTON       = 12
TOUCHPAD_PRESS      = 13

# PID Control
Kp_turn = 65
Kp_line = 65
Kd = 4
Ki = 0
ALPHA = 1  # alpha of the moving mean for the turn coefficient
# Main Program
FPS = 40
N_SECONDS = 3000  # number of seconds before exiting the program
BAUDRATE = 115200  # Communication with the Arduino
# Number of messages we can send to the Arduino without receiving an acknowledgment
N_MESSAGES_ALLOWED = 3
COMMAND_QUEUE_SIZE = 2
