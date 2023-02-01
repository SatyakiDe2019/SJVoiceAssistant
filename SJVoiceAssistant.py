#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 26-Dec-2022                     ####
#### Modified On 31-Jan-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### multiple classes to initiate the            ####
#### AI-enabled personal assistant, which would  ####
#### display & answer the queries through voice. ####
#####################################################

import pyaudio
from six.moves import queue
import ssl
import json
import pandas as p
import clsMicrophoneStream as ms
import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime
import clsChatEngine as ce
import clsText2Voice as tv
import clsVoice2Text as vt
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL)

###################################################
##### Adding the Instantiating Global classes #####
###################################################
x2 = ce.clsChatEngine()
x3 = tv.clsText2Voice()
x4 = vt.clsVoice2Text()
# Initiating Log class
l = cl.clsL()
###################################################
#####        End of Global Classes          #######
###################################################
# Bypassing SSL Authentication
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

######################################
### Insert your access token here ####
######################################
debug_ind = 'Y'
######################################
####         Global Flag      ########
######################################

def main():
    try:
        spFlag = True

        var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('Start Time: ' + str(var))
        print('*'*120)

        exitComment = 'THANKS.'

        while True:
            try:
                finalText = ''

                if spFlag == True:
                    finalText = x4.processVoice(var)
                else:
                    pass

                val = finalText.upper().strip()

                print('Main Return: ', val)
                print('Exit Call: ', exitComment)
                print('Length of Main Return: ', len(val))
                print('Length of Exit Call: ', len(exitComment))

                if val == exitComment:
                    break
                elif finalText == '':
                    spFlag = True
                else:
                    print('spFlag::',spFlag)
                    print('Inside: ', finalText)
                    resVal = x2.findFromSJ(finalText)

                    print('ChatGPT Response:: ')
                    print(resVal)

                    resAud = x3.getAudio(resVal)
                    spFlag = False
            except Exception as e:
                pass

        var1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print('*'*120)
        print('End Time: ' + str(var1))
        print('SJ Voice Assistant exited successfully!')
        print('*'*120)

    except Exception as e:
        x = str(e)
        print('Error: ', x)

if __name__ == "__main__":
    main()
