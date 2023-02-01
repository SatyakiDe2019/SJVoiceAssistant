################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 31-Dec-2022               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal AI-driven voice assistant.    ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'output' + sep,
        'REPORT_DIR': 'output',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'CODE_PATH': Curr_Path + sep + 'Code' + sep,
        'APP_DESC_1': 'Personal Voice Assistant (SJ)!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'TITLE': "Personal Voice Assistant (SJ)!",
        'PATH' : Curr_Path,
        'OPENAI_API_KEY': "sk-aapwfMWDuFE5XXXUr2BH",
        'REVAI_API_KEY': "02ks6kFhEKjdhdure8474JJAJJ945958_h8P_DEKDNkK6DwNNNHU17aRtCw",
        'MODEL_NAME': "code-davinci-002",
        "speedSpeech": 170,
        "speedPitch": 0.8,
        "soundRate": 44100,
        "contentType": "audio/x-raw",
        "layout": "interleaved",
        "format": "S16LE",
        "channels": 1
    }
