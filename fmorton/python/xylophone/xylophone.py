from BirdBrain import Hummingbird, Microbit
import time

# song examples available at youcanplayit.com
#
# note positions (0=lowest note, 7=highest) CDEFGABc
#

class Xylophone:
    ROTATE_SERVO = 1
    PLAY_SERVO = 2
    SERVO_DOWN_TIME = 0.099
    SERVO_MOVE_TIME = 0.40
    REST = 999

    #DOWN = [ 99, 99, 99, 99, 99, 99, 97, 96 ]
    #UP = [ 120, 120, 120, 120, 120, 120, 120, 120 ]
    #ROTATE = [ 5, 20, 38, 60, 90, 120, 148, 167 ]

    DOWN = [ 96, 97, 99, 99, 99, 99, 99, 99 ]
    UP = [ 120, 120, 120, 120, 120, 120, 120, 120 ]
    ROTATE = [ 167, 148, 120, 90, 60, 38, 20, 5 ]

    def __init__(self):
        self.hum = Hummingbird('A')


    def play_note(self, position):
        if position == self.REST:
            time.sleep(self.SERVO_MOVE_TIME)
        else:
            down = self.DOWN[position]
            up = self.UP[position]
            rotate = self.ROTATE[position]

            self.hum.setPositionServo(self.ROTATE_SERVO, rotate)
            time.sleep(self.SERVO_MOVE_TIME)

            self.hum.setPositionServo(self.PLAY_SERVO, down)
            time.sleep(self.SERVO_DOWN_TIME)
            self.hum.setPositionServo(self.PLAY_SERVO, up)


    def play_song(self, song):
        self.hum.setPositionServo(self.ROTATE_SERVO, self.ROTATE[song[0]])

        time.sleep(self.SERVO_MOVE_TIME)

        for note in song:
            self.play_note(note)


    def stop_song(self):
        self.hum.stopAll()


