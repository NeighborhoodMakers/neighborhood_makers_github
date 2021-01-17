from BirdBrain import Hummingbird, Microbit
import time

ROTATE_SERVO = 1
PLAY_SERVO = 2
SERVO_DOWN_TIME = 0.1
SERVO_MOVE_TIME = 0.40
REST = 999

DOWN = [ 99, 99, 99, 99, 99, 99, 97, 96 ]
UP = [ 120, 120, 120, 120, 120, 120, 120, 120 ]
ROTATE = [ 5, 20, 38, 60, 90, 120, 148, 167 ]

hum = Hummingbird('A')

def play_note(position):
    if position == REST:
        time.sleep(SERVO_MOVE_TIME)
    else:
        down = DOWN[position]
        up = UP[position]
        rotate = ROTATE[position]

        hum.setPositionServo(ROTATE_SERVO, rotate)
        time.sleep(SERVO_MOVE_TIME)

        hum.setPositionServo(PLAY_SERVO, down)
        time.sleep(SERVO_DOWN_TIME)
        #time.sleep(1.25)
        hum.setPositionServo(PLAY_SERVO, up)
        #time.sleep(1.25)


def play_song(song):
    hum.setPositionServo(ROTATE_SERVO, ROTATE[song[0]])
    time.sleep(SERVO_MOVE_TIME)

    for note in song:
        play_note(note)


#time.sleep(5.0)

# twinkle twinkle little star
song = [ 7,7,3,3,2,2,3,REST,4,4,5,5,6,6,7,REST,3,3,4,4,5,5,6,REST,3,3,4,4,5,5,6,REST,7,7,3,3,2,2,3,REST,4,4,5,5,6,6,7 ]

#play_song(song)

scales = [ 0,1,2,3,4,5,6,7,6,5,4,3,2,1,0 ]

play_song(scales)

play_song([ 0,1,0,1,2,2,3,4,3,4,5,4,5,6,5,6,7,6,7 ])

#play_song([ 0, 0, 0, 1, 2, 3, 4, 5, 6, 7 ])

#for i in range(8):
#    print("play")
#    play_song([ 0, 0, 0, 1, 2, 3, 4, 5, 6, 7 ])
#    time.sleep(1.0)


#song = [ 7, 6, 5, 4, 3, 2, 1, 0 ]

#play_song(song)

#for i in range(8):
#    play_note(7)

        
hum.stopAll()
