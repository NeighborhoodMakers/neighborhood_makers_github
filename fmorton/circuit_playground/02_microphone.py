import array
import math
import time

import audiobusio
import board

class MicrophoneSound:
    SAMPLE_COUNT = 160
    MAXIMUM_LEVEL_CHANGE = 100
    STARTING_LOWEST_AVERAGE = 33200
    NORMALIZED_AVERAGE_STACK_SIZE = 3


    def __init__(self, stack_size = NORMALIZED_AVERAGE_STACK_SIZE):
        self.samples = array.array('H', [0] * self.SAMPLE_COUNT)
        self.lowest_normalized_average = self.STARTING_LOWEST_AVERAGE
        self.adjusted_normalized_average_stack = [0] * stack_size

        self.record_samples(open_microphone=True)


    def record_samples(self, open_microphone = False):
        # For CircuitPython 2.x:
        #self.mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
        #                       frequency=16000, bit_depth=16)
        # For Circuitpython 3.0 and up, "frequency" is now called "sample_rate".
        # Comment the lines above and uncomment the lines below.
        if open_microphone:
            self.mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                                        sample_rate=16000, bit_depth=16)

        self.mic.record(self.samples, len(self.samples))


    def normalize(self, values, sliding_lowest_average=False):
        #normalize_chunk_size = int(len(values) / 4)
        #print("normalize_chunk_size is ", str(normalize_chunk_size))
        #sorted_values = sorted(values)[normalize_chunk_size:(normalize_chunk_size*3)]
        #print(values,)
        #print(sorted_values,)
        #minbuf = int(self.mean(values))
        #samples_sum = sum(
        #    float(sample - minbuf) * (sample - minbuf)
        #    for sample in values
        #)

        #if (sorted_values[-1] < self.lowest_level) and (sorted_values[-1] > 0):
        #    self.lowest_level = sorted_values[-1]

        #normalized_average = (sum(sorted_values) / len(sorted_values))
        #normalized_average = sorted_values[int(len(sorted_values)/2)]
        #normalized_average = sorted(values)[int(len(values)/2)]
        normalized_average = sum(values) / len(values)

        if (normalized_average < self.lowest_normalized_average):
            level_change = self.lowest_normalized_average - normalized_average
            #print("level_change is ", str(level_change), " !!!!!!!!!!!!!!!!!!!")
            #print(sorted(values))
            if level_change < self.MAXIMUM_LEVEL_CHANGE:
                #print("DEBUG: sliding_lowest_average is !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! " + str(sliding_lowest_average))
                if sliding_lowest_average:
                    self.lowest_normalized_average = normalized_average
            else:
                normalized_average = self.lowest_normalized_average


        #if normalized_average < 0:
        #    normalized_average = self.lowest_level
        #elif (normalized_average < self.lowest_level):
        #    self.lowest_level = normalized_average


        #adjusted_normalized_average = normalized_average - self.lowest_level

        #if(adjusted_normalized_average < 0):
        #    adjusted_normalized_average = self.lowest_level

        #print("DEBUG: normalized_average is=================================== ", str(normalized_average), str(self.lowest_normalized_average), str(normalized_average - self.lowest_normalized_average))

        #if (normalized_average < 0):
        #    return 0

        #print("sorted_values[-1] is ", str(sorted_values[-1]))
        #print("self.lowest_level is........................................................... " + str(self.lowest_level))

        #if(normalized_average < self.lowest_normalized_average):
        #    self.lowest_normalized_average = normalized_average
        #print((str(normalized_average), str(adjusted_normalized_average), str(self.lowest_level),))

        #return math.sqrt(samples_sum / len(values))
        #return (samples_sum / len(values))
        #return(normalized_average - self.lowest_normalized_average)
        adjusted_normalized_average = normalized_average - self.lowest_normalized_average
 
        if adjusted_normalized_average < 0:
            adjusted_normalized_average = 0

        #if self.adjusted_normalized_average_stack is None:
        #    self.adjusted_normalized_average_stack = [adjusted_normalized_average] * self.NORMALIZED_AVERAGE_STACK_SIZE

        self.adjusted_normalized_average_stack.pop()
        self.adjusted_normalized_average_stack.insert(0, adjusted_normalized_average)

        #print("self.adjusted_normalized_average_stack is ", self.adjusted_normalized_average_stack)
        return(sum(self.adjusted_normalized_average_stack) / len(self.adjusted_normalized_average_stack))


    #def mean(self, values):
    #    return sum(values) / len(values)

    def magnitude(self):
        self.mic.record(self.samples, len(self.samples))

        return(self.normalize(self.samples))


# For CircuitPython 2.x:
#mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
#                       frequency=16000, bit_depth=16)
# For Circuitpython 3.0 and up, "frequency" is now called "sample_rate".
# Comment the lines above and uncomment the lines below.
#mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
#                       sample_rate=16000, bit_depth=16)

# Record an initial sample to calibrate. Assume it's quiet when we start.
#samples = array.array('H', [0] * NUM_SAMPLES)

sound = MicrophoneSound()

counter = 0
total = 0.0

#while True:
while (counter < 2500):
    counter = counter + 1

    #mic.record(samples, len(samples))
    #magnitude = normalize(samples)
    magnitude = sound.magnitude()
    print((magnitude,), " ", str(counter))
    #print((magnitude,))

    # You might want to print this to see the values.
    # print(magnitude)
    #time.sleep(0.4)

    if (counter > 1500):
        total = total + magnitude

print(str(total / 1000))

'''
32dB = 26.4580, 28.1753 | 25.2947, 25.0494          | 27.9044, 28.5906, 27.0797
44dB = 26.1288, 26.9857 | 26.3147, 25.6575, 25.5428 | 28.8652, 28.3285
55dB = 28.1222, 27.5773 | 25.2559, 25.275           | 28.4146, 26.4064
69dB = 27.9259, 28.1537
83dB = 46.7561, 51.0671
92dB = 87.3807, 88.1442 | 85.4243, 93.7714

'''