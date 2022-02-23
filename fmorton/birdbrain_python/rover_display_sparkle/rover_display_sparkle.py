from BirdBrain import Finch
import random

finch = Finch()

for x in range(500):
    row = random.randint(1,5)
    col = random.randint(1,5)
    value = random.randint(0,1)

    finch.setPoint(row, col, value)

for row in range(5):
    for col in range(5):
        finch.setPoint(row + 1, col + 1, 0)

