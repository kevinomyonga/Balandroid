"""
File containing all the constants used in the different files
"""

# PS4 Controller Button Configuration
PS4_SQUARE              = 0
PS4_X                   = 1
PS4_CIRCLE              = 2
PS4_TRIANGLE            = 3
PS4_L1                  = 4
PS4_R1                  = 5
PS4_L2                  = 6
PS4_R2                  = 7
PS4_SHARE               = 8
PS4_OPTIONS             = 9
PS4_L3                  = 10
PS4_R3                  = 11
PS4_ON_BUTTON       	= 12
PS4_TOUCHPAD_PRESS      = 13

# XBOX One Controller Button Configuration =
XBOX_A                   = 0
XBOX_B                   = 1
XBOX_X                   = 2
XBOX_Y                   = 3
XBOX_LB                  = 4
XBOX_RB                  = 5
XBOX_LT                  = 6
XBOX_RT                  = 7
XBOX_VIEW                = 8
XBOX_MENU                = 9
XBOX_LTHUMBSTICK         = 10
XBOX_RTHUMBSTICK         = 11

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
