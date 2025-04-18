import sounddevice as sd
from scipy.io.wavfile import write
fs=44100
seconds= int(input("enter time duration in seconds"))
print("recording...... \n")

record_voice= sd.rec(int(seconds*fs), samplerate=fs, channels=2, dtype='int16')

sd.wait()

write("out.wav", fs, record_voice)

print("finished... \n Please check 'out.wav' ." )