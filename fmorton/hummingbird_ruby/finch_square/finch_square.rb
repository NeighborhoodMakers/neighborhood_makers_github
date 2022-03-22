require 'birdbrain'

finch = BirdbrainFinch.connect('A')

finch.beak(0, 50, 0)

finch.tail(1, 0, 50, 0)
finch.move(BirdbrainFinch::FORWARD, 2, 20)
finch.turn(BirdbrainFinch::LEFT, 90, 50)

finch.tail(2, 0, 50, 0)
finch.move(BirdbrainFinch::FORWARD, 2, 20)
finch.turn(BirdbrainFinch::RIGHT, 90, 50)
finch.tail(3, 0, 50, 0)

finch.move(BirdbrainFinch::BACKWARD, 2, 20)
finch.turn(BirdbrainFinch::RIGHT, 90, 50)
finch.tail(4, 0, 50, 0)

finch.move(BirdbrainFinch::FORWARD, 2, 20)
finch.turn(BirdbrainFinch::LEFT, 90, 50)
sleep(1)

finch.disconnect

def draw(finch, step, move_direction, turn_direction)
  finch.tail(step, 0, 50, 0)
  finch.move(move_direction, 2, 20)
  finch.turn(turn_direction, 90, 50)
end

finch = BirdbrainFinch.connect('A')

finch.beak(0, 50, 0)

draw(finch, 1, BirdbrainFinch::FORWARD, BirdbrainFinch::LEFT)
draw(finch, 2, BirdbrainFinch::FORWARD, BirdbrainFinch::RIGHT)
draw(finch, 3, BirdbrainFinch::BACKWARD, BirdbrainFinch::RIGHT)
draw(finch, 4, BirdbrainFinch::FORWARD, BirdbrainFinch::LEFT)

finch.disconnect
