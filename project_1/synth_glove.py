"""
--------------------------------------------------------------------------
Keyboard Glove
--------------------------------------------------------------------------
License:   
Copyright 2019 - Eric Voigt

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Modulate sound output with variable flex input

  - Potentiometer signals connected to AIN0, AIN1, AIN2, AIN3, AIN4
  - USB audio adapter connected to USB1 (P1_5, P1_7, P1_9, P1_11, P1_13, P1_15)

When potentiometers are changed, the audio output will change

--------------------------------------------------------------------------
Background:
  - Analog servo control class demonstration (analog_servo_control.py)
  - PocketBeagle audio driver setup (http://einsteiniumstudios.com/make-your-beaglebone-speak.html)

"""
# ------------------------------------------------------------------------
# Packages
# ------------------------------------------------------------------------

import time
import Adafruit_BBIO.ADC as ADC

# ------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------

debug       = True

update_time = 0.1

# ------------------------------------------------------------------------
# Pin Assignments
# ------------------------------------------------------------------------

# Analog setup for flex sensing
A_THUMB   = "P1_27"                      # AIN_4
A_INDEX   = "P1_25"                      # AIN_3
A_MIDDLE  = "P1_23"                      # AIN_2
A_RING    = "P1_21"                      # AIN_1
A_PINKY   = "P1_19"                      # AIN_0

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def setup():
    """Set up the hardware components."""
    ADC.setup()

# end def

# ------------------------------------------------------------------------

def print_pots(A_THUMB, A_INDEX, A_MIDDLE, A_RING, A_PINKY):
    """Scale and print the potentiometer signals for testing."""
    thumb_flex           = float(ADC.read(A_THUMB))
    index_flex           = float(ADC.read(A_INDEX))
    middle_flex          = float(ADC.read(A_MIDDLE))
    ring_flex            = float(ADC.read(A_RING))
    pinky_flex           = float(ADC.read(A_PINKY))

    
    if (debug):
        print("thumb = {0}; index = {1}; middle = {2}; ring = {3}; pinky = {4}".format(thumb_flex, index_flex, middle_flex, ring_flex, pinky_flex))

# end def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setup()
    print("Synth Glove Testbed Program Start")

    while True:
        print_pots(A_THUMB, A_INDEX, A_MIDDLE, A_RING, A_PINKY)
        time.sleep(update_time)

    print("Servo Control Program Finished")