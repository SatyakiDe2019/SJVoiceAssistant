#####################################################
#### Written By: SATYAKI DE                      ####
#### Written On: 26-Dec-2022                     ####
#### Modified On 28-Jan-2023                     ####
####                                             ####
#### Objective: This is the main calling         ####
#### python script that will invoke the          ####
#### Rev-AI class to initiate the transformation ####
#### of audio into the text.                     ####
#####################################################

import pyaudio
from rev_ai.models import MediaConfig
from rev_ai.streamingclient import RevAiStreamingClient
from six.moves import queue
import ssl
import json
import pandas as p
import clsMicrophoneStream as ms
import clsL as cl
from clsConfigClient import clsConfigClient as cf
import datetime

# Initiating Log class
l = cl.clsL()

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
################################################################
### Sampling rate of your microphone and desired chunk size ####
################################################################

class clsVoice2Text:
    def __init__(self):
        self.OPENAI_API_KEY=str(cf.conf['OPENAI_API_KEY'])
        self.rate = cf.conf['soundRate']

    def processVoice(self, var):
        try:
            OPENAI_API_KEY = self.OPENAI_API_KEY
            accessToken = cf.conf['REVAI_API_KEY']
            rate = self.rate
            chunk = int(rate/10)

            ################################################################
            ### Creates a media config with the settings set for a raw  ####
            ### microphone input                                        ####
            ################################################################

            sampleMC = MediaConfig('audio/x-raw', 'interleaved', 44100, 'S16LE', 1)

            streamclient = RevAiStreamingClient(accessToken, sampleMC)

            #####################################################################
            ### Opens microphone input. The input will stop after a keyboard ####
            ### interrupt.                                                   ####
            #####################################################################

            with ms.clsMicrophoneStream(rate, chunk) as stream:

                #####################################################################
                ### Uses try method to enable users to manually close the stream ####
                #####################################################################

                try:
                    response_gen = ''
                    response = ''
                    finalText = ''
                    #########################################################################
                    ### Starts the server connection and thread sending microphone audio ####
                    #########################################################################

                    response_gen = streamclient.start(stream.generator())

                    ###################################################
                    ### Iterates through responses and prints them ####
                    ###################################################

                    for response in response_gen:
                        try:
                            print('JSON:')
                            print(response)

                            r = json.loads(response)

                            df = p.json_normalize(r["elements"])
                            l.logr('1.df_' + var + '.csv', debug_ind, df, 'log')
                            column_name = "confidence"

                            if column_name in df.columns:
                                print('DF:: ')
                                print(df)

                                finalText = "".join(df["value"])
                                print("TEXT:")
                                print(finalText)

                                df = p.DataFrame()

                                raise Exception

                        except Exception as e:
                            x = str(e)
                            break

                    streamclient.end()

                    return finalText

                except Exception as e:
                    x = str(e)
                    #######################################
                    ### Ends the WebSocket connection. ####
                    #######################################

                    streamclient.end()

                    return ''

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            streamclient.end()

            return x
