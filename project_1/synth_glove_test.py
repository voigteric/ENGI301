"""
--------------------------------------------------------------------------
Synth Glove Test Setup with Potentiometers
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
Modulate sound output with potentiometer input

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
import os

# ------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------

debug       = False

update_time = 0.025

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
    """set up the hardware components"""
    ADC.setup()

# end def

def play_sounds(thumb_flex, thumb_prev, index_flex, index_prev, middle_flex, middle_prev, ring_flex, ring_prev, pinky_flex, pinky_prev):
    """check to see change in finger flex. if so, play associated sound"""
    if (thumb_flex >= 0.65)  and (thumb_prev < 0.65):
        os.system("aplay /var/lib/cloud9/ENGI301/project_01/808.wav")
    if (index_flex >= 0.65)  and (index_prev < 0.65):
        os.system("aplay /var/lib/cloud9/ENGI301/project_01/tom.wav")
    if (middle_flex >= 0.65) and (middle_prev < 0.65):
        os.system("aplay /var/lib/cloud9/ENGI301/project_01/snare.wav")
    if (ring_flex >= 0.65)   and (ring_prev < 0.65):
        os.system("aplay /var/lib/cloud9/ENGI301/project_01/hi_hat.wav")
    if (pinky_flex >= 0.65)  and (pinky_prev < 0.65):
        os.system("aplay /var/lib/cloud9/ENGI301/project_01/hand_clap.wav")

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setup()
    print("Synth Glove Testbed Program Start")
    
    t_p = 0
    i_p = 0
    m_p = 0
    r_p = 0
    p_p = 0

    while True:
        """scale and print the potentiometer signals for testing"""
        t_f = float(ADC.read(A_THUMB))
        i_f = float(ADC.read(A_INDEX))
        m_f = float(ADC.read(A_MIDDLE))
        r_f = float(ADC.read(A_RING))
        p_f = float(ADC.read(A_PINKY))
        
        """debugging display"""
        if (debug):
            print("thumb = {0}; index = {1}; middle = {2}; ring = {3}; pinky = {4}".format(t_f, i_f, m_f, r_f, p_f))
        
        play_sounds(t_f, t_p, i_f, i_p, m_f, m_p, r_f, r_p, p_f, p_p)
        
        """store previous values for next step"""
        t_p = t_f
        i_p = i_f
        m_p = m_f
        r_p = r_f
        p_p = p_f
        
        time.sleep(update_time)

    print("Synth Glove Testbed Program Finished")