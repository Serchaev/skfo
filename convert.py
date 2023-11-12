# import required modules
import subprocess

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'target.mp3', 'target.wav'])
