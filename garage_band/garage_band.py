#!../.venv/bin/python3

import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal,fft
import numpy as np
import librosa



#read file and get duration
path_to_audio = 'diapason.wav'
data, fs = sf.read(path_to_audio)
f = sf.SoundFile(path_to_audio)
duration = f.frames/f.samplerate


#write new audio file
sf.write('ciao.wav',data,fs)

#select channel, get fft and plot all
channel_sx = data[:,0]
channel_dx = data[:,1]
freq = fft.rfftfreq(len(channel_sx),1/fs)
t = np.linspace(0,duration,len(channel_sx))
fft_sx = fft.rfft(channel_sx,norm='forward')
fft_dx = fft.rfft(channel_dx,norm='forward')
#find peak and peaks width
peaks = signal.find_peaks(abs(fft_sx)**2, height = 2.8e-5)[0]
print('Picchi: ',peaks, 'Numero Picchi: ', len(peaks))
peaks_widths = signal.peak_widths(abs(fft_sx)**2,peaks, rel_height = .99)[0]
print('Larghezze picchi: ', peaks_widths)
#convert peak frequencies to musical notes
notes = librosa.hz_to_note(freq[peaks])
print('Note corrispondenti ai picchi: ',notes)

#filter main peak and write new file audio
nyq = 0.5 * fs  # Nyquist Frequency
def get_peak_freq(segnale,picchi):
    max = 0
    max_index = 0
    i = 0
    for i in range(len(picchi)):
        value = abs(segnale[picchi[i]])**2
        if max< value:
            max_index = i
            max = picchi[i]
    return max, max_index


target_freq, target_freq_index= get_peak_freq(fft_sx, peaks)
target_width = peaks_widths[target_freq_index]

print(target_freq,target_freq_index, target_width)

#TODO left_ips
filter = [1 if i< abs(target_freq+target_width) else 0 for i in freq]
fft_filtered_signal = [fft_sx * filter,fft_dx * filter]
filtered_signal = [fft.irfft(i).real.astype('int16') for i in fft_filtered_signal]

#writing new file with file audio
sf.write('filter.wav',filtered_signal, fs)

plt.figure(figsize=(16, 9))
plt.plot(freq,filter)
plt.ylabel("")
plt.xlabel("frequency")
plt.title("filter")


plt.figure(figsize=(16, 9))
plt.plot(freq,abs(filtered_signal)**2)
plt.ylabel("")
plt.xlabel("frequency")
plt.title("filtered Signal")


# plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
# plt.plot(t,channel_sx)
# plt.ylabel("sound")
# plt.xlabel("time(s)")
# plt.figure()

# plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
# plt.plot(freq,abs(fft_sx)**2)
# plt.plot(freq[peaks],abs(fft_sx[peaks])**2, 'x')
# plt.ylabel("")
# plt.xlabel("frequency")
# plt.title("potenza")
# plt.figure()

# plt.plot(freq, abs(fft_sx))
# plt.ylabel("")
# plt.xlabel("frequency")
# plt.title("Real")
# plt.figure()

# plt.plot(freq, fft_sx.imag)
# plt.ylabel("")
# plt.xlabel("frequency")
# plt.title("imag")
# plt.show()


plt.show()
