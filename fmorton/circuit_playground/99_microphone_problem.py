import array
import math
import time

import audiobusio
import board

SAMPLE_COUNT = 10

samples = array.array('H', [0] * SAMPLE_COUNT)

mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                            sample_rate=16000, bit_depth=16)

while True:
    mic.record(samples, len(samples))

    print(samples)

    sorted_samples = sorted(samples)

    middle_value = sorted_samples[int(len(sorted_samples)/2)]

    print((middle_value,))

    time.sleep(3.5)