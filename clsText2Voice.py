###############################################
#### Written By: SATYAKI DE                ####
#### Written On: 27-Oct-2019               ####
#### Modified On 28-Jan-2023               ####
####                                       ####
#### Objective: Main class converting      ####
#### text to voice using third-party API.  ####
###############################################

import pyttsx3
from clsConfigClient import clsConfigClient as cf

class clsText2Voice:
    def __init__(self):
        self.speedSpeech = cf.conf['speedSpeech']
        self.speedPitch = cf.conf['speedPitch']

    def getAudio(self, srcString):
        try:
            speedSpeech = self.speedSpeech
            speedPitch = self.speedPitch
            
            engine = pyttsx3.init()

            # Set the speed of the speech (in words per minute)
            engine.setProperty('rate', speedSpeech)

            # Set the pitch of the speech (1.0 is default)
            engine.setProperty('pitch', speedPitch)

            # Converting to MP3
            engine.say(srcString)
            engine.runAndWait()

            return 0

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1
