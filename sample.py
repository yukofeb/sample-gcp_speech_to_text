#!/usr/bin/env python

##########
# $ GOOGLE_APPLICATION_CREDENTIALS='/path/to/gcp_auth.json' python sample.py speechsample01.flac
##########

import sys
import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def get_text(file_name):
    client = speech.SpeechClient()

    file_path = os.path.join(
        os.path.dirname(__file__),
        'resources',
        file_name)

    with io.open(file_path, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='ja-JP')

    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        print('Confidence: {}'.format(result.alternatives[0].confidence))

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        get_text(args[1])
    else:
        print('error: expected one argument.')
