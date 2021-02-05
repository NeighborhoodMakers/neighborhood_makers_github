class Xylophone
  ROTATE_SERVO = 1
  PLAY_SERVO = 2
  SERVO_DOWN_TIME = 0.099
  SERVO_MOVE_TIME = 0.40
  REST = 999

  DOWN = [ 96, 97, 99, 99, 99, 99, 99, 99 ]
  UP = [ 120, 120, 120, 120, 120, 120, 120, 120 ]
  ROTATE = [ 167, 148, 120, 90, 60, 38, 20, 5 ]

  def initialize
    @hummingbird = BirdbrainHummingbird.connect
  end

  def play_note(position)
    if position == REST
      sleep(SERVO_MOVE_TIME)
    else
      down = DOWN[position]
      up = UP[position]
      rotate = ROTATE[position]

      @hummingbird.position_servo(ROTATE_SERVO, rotate)
      sleep(SERVO_MOVE_TIME)

      @hummingbird.position_servo(PLAY_SERVO, down)
      sleep(SERVO_DOWN_TIME)
      @hummingbird.position_servo(PLAY_SERVO, up)
    end
  end

  def play_song(song)
    @hummingbird.position_servo(ROTATE_SERVO, ROTATE[song[0]])

    sleep(SERVO_MOVE_TIME)

    for note in song
      play_note(note)
    end
  end

  def stop_song
    @hummingbird.position_servo(ROTATE_SERVO, ROTATE[3])
  end
end
