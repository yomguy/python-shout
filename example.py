#!/usr/bin/env python

# usage: ./example.py /path/to/file1 /path/to/file2 ...
import shout
import sys
import string
import time

s = shout.Shout()
print("Using libshout version %s" % shout.version())

s.host = 'localhost'
s.port = 8000
s.user = 'source'
s.password = 'MYPASSWORD'
s.mount = "/pyshout"
s.format = 'mp3'
s.protocol = 'http'
s.name = ''
s.genre = ''
s.url = ''
s.public = 0
s.audio_info = {shout.SHOUT_AI_BITRATE:'128', shout.SHOUT_AI_SAMPLERATE:'44100', shout.SHOUT_AI_CHANNELS:'2'}
# (keys are shout.SHOUT_AI_BITRATE, shout.SHOUT_AI_SAMPLERATE,
#  shout.SHOUT_AI_CHANNELS, shout.SHOUT_AI_QUALITY)

s.open()
s.get_connected()

total = 0
st = time.time()
for fa in sys.argv[1:]:
    print("opening file %s" % fa)
    f = open(fa, 'rb')
    s.set_metadata({'song': fa})

    nbuf = f.read(4096)
    while 1:
        buf = nbuf
        nbuf = f.read(4096)
        total = total + len(buf)
        if len(buf) == 0:
            break
        s.send(buf)
        s.sync()
    f.close()

    et = time.time()
    br = total*0.008/(et-st)
    print("Sent %d bytes in %d seconds (%f kbps)" % (total, et-st, br))

s.close()
