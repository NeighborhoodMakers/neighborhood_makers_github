import array
import math
import time

import audiobusio
import board

NUM_SAMPLES = 250
LOWEST_LEVEL = 33200

def normalize(values):
    normalize_chunk_size = int(len(values) / 4)
    #print("normalize_chunk_size is ", str(normalize_chunk_size))
    sorted_values = sorted(values)[normalize_chunk_size:(normalize_chunk_size*3)]
    print(sorted_values,)
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    normalized_average = (sum(sorted_values) / len(sorted_values)) - LOWEST_LEVEL
    #print("DEBUG: normalized_average is=================================== ", str(normalized_average))

    #if (sorted_values[0] < LOWEST_LEVEL):
    #    LOWEST_LEVEL = sorted_values[0]

    #print("lowest_level is " + LOWEST_LEVEL)

    if (normalized_average < 0):
        return 0

    #return math.sqrt(samples_sum / len(values))
    #return (samples_sum / len(values))
    return(normalized_average)


def mean(values):
    return sum(values) / len(values)


# For CircuitPython 2.x:
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       frequency=16000, bit_depth=16)
# For Circuitpython 3.0 and up, "frequency" is now called "sample_rate".
# Comment the lines above and uncomment the lines below.
#mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
#                       sample_rate=16000, bit_depth=16)

# Record an initial sample to calibrate. Assume it's quiet when we start.
samples = array.array('H', [0] * NUM_SAMPLES)

while True:
    mic.record(samples, len(samples))
    magnitude = normalize(samples)
    print((magnitude,))

    # You might want to print this to see the values.
    # print(magnitude)
    time.sleep(0.5)
