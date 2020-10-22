# -*- coding: utf-8 -*-
import os
import glob
from pydub import AudioSegment
from pydub import audio_segment  # Import this module first

# # Load two mp3 audios that need to be merged
# # input_music_1 = AudioSegment.from_ogg("audio/1.ogg") 
# commonaudio = AudioSegment.from_ogg("common.ogg") 

# output_music = commonaudio + commonaudio
# # Simple input audio after merging
# output_music.export("./merged/output_music.ogg", format="ogg")# Save path, followed by save format

audiofiles = './audio-files/' 
commonaudio = AudioSegment.from_ogg("common.ogg")
i=1
for filename in os.listdir(audiofiles):
    audio = os.path.join(audiofiles, filename)
    print(audio)
    tomergeaudio = AudioSegment.from_file(audio)
    merged_audio = tomergeaudio + commonaudio
    merged_audio.export("./merged/merged_audio"+str(i)+".ogg",format="ogg") 
    i+=1
