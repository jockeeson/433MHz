#!/usr/bin/env python

import time
import sys
import RPi.GPIO as GPIO

a_on =  '201011010101010011001011001010101101001100101011010010110010101010'
a_off = '201011010101010011001011001010101101001100101011010010101010101010'
b_on =  '201011010101010011001011001010101101001100101011010010110010101100'
b_off = '201011010101010011001011001010101101001100101011010010101010101100'
c_on =  '201011010101010011001011001010101101001100101011010010110010110010'
c_off = '201011010101010011001011001010101101001100101011010010101010110010'
all_off='201011010101010011001011001010101101001100101011010011001010101010'
pulse = 0.000283
short_pause = 0.000255
long_pause = 0.001304
xlong_pause = 0.002696
extended_pause = 0.01044
#short_delay = 0.00045
#long_delay = 0.00090
#extended_delay = 0.0096

NUM_ATTEMPTS = 3
TRANSMIT_PIN = 11

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '2':
				    GPIO.output(TRANSMIT_PIN, 1)
				    time.sleep(pulse)
				    GPIO.output(TRANSMIT_PIN, 0)
				    time.sleep(xlong_pause)
            elif i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_pause)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_pause)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_pause)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

