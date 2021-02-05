import sys
import time
import board
import pulseio
import adafruit_irremote

def read_pulses(input_pulses, max_pulse=10000, blocking=True, blocking_sleep=0.10, recent_sleep=0.10):
    while True:
        pulses = read_pulses_non_blocking(input_pulses, max_pulse, recent_sleep)
        if blocking and pulses is None:
            time.sleep(blocking_sleep)
            continue
        return pulses

def read_pulses_non_blocking(input_pulses, max_pulse=10000, recent_sleep=0.10):
    received = None
    recent_count = 0
    pruning = False
    while True:
        try:
            pulse = input_pulses.popleft()
            recent_count += 1
            if pulse > max_pulse:
                if received is None:
                    continue
                pruning = True
            if not pruning:
                if received is None:
                    received = []
                received.append(pulse)
        except IndexError as e:
            if recent_count == 0:
                return received
            recent_count = 0
            time.sleep(recent_sleep)


def read_pulses_adafruit(input_pulses, max_pulse=10000, blocking=True):
    if not input_pulses and not blocking:
        return None
    received = []
    while True:
        while not input_pulses:
            pass
        while input_pulses:
            pulse = input_pulses.popleft()
            if pulse > max_pulse:
                if not received:
                    continue
                else:
                    return received
            received.append(pulse)
    return received


input_pulses = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = read_pulses(input_pulses, blocking=False)
    #pulses = read_pulses_adafruit(input_pulses, blocking=False)

    if pulses is None:
        print("Processing other stuff...")
    else:
        try:
            code = decoder.decode_bits(pulses, debug=False)
            print("code is", code)
        except adafruit_irremote.IRNECRepeatException:
            pass
        except adafruit_irremote.IRDecodeException as e:
            pass

    time.sleep(0.25)