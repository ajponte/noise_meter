#!/bin/bash

import wave
from chunk import Chunk

wave_read = wave.open('it.wav', 'rb')
frame_rate = wave_read.getframerate()
n_frames = wave_read.getnframes()
wave_read.close()

print "frame rate: " + str(frame_rate)
print "number of frames: " + str(n_frames)

import scipy.io.wavfile
import numpy as np
import math

rate, data = scipy.io.wavfile.read('it.wav')
chunks = np.array_split(data,4)
#dbs = [20*np.log10( math.sqrt(np.mean(chunk**2)) ) for chunk in chunks]
dbs = []

for chunk in chunks:
   db_level = 0
   try:
      db_level = 20*np.log10(math.sqrt(np.mean(chunk**2)))
   except:
      deb_level = 0
   dbs.append(db_level)
#try:
#   a='foo'
	#samprate, wavdata = read('/Users/alan.ponte/hackday/audio_test/sound1.wav')
#except:
  # print "wavdata: " + wavdata

#import numpy as np
#chunks = np.array_split(wavdata, numchunks)
#dbs = [20*log10( sqrt(mean(chunk**2)) ) for chunk in chunks]

#print "dbs: " + dbs
