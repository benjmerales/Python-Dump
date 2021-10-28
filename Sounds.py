from playsound import playsound
import simpleaudio as sa
import sounddevice as sd 
import soundfile as sf 

file = 'C:\\Users\\Lenovo.DESKTOP-EAORNA8\\Music\\11 - 25 - 19\\Los Campesinos - You! Me! Dancing!.mp3'
# Using Playsound
playsound()

# Using Simple Audio
wav_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()

#using Sound Device
data, fs = sf.read(file, dtype='float32')
sd.play(data, fs)
status = sd.wait()