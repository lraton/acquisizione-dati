#!.venv/bin/python3

from scipy.io.wavfile import write as write_wav
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal,fft
import numpy as np
import librosa, time
import wave
import soundcard as sc

# get the current default speaker on your system:
default_speaker = sc.default_speaker()

#read file and get duration
path_to_audio = 'pulita_semplice.wav'
data, fs = sf.read(path_to_audio)
f = sf.SoundFile(path_to_audio)
duration = f.frames/f.samplerate


#write new audio file
sf.write('new_diapason.wav',data,fs)

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
left_peaks , right_peaks = signal.peak_widths(abs(fft_sx)**2,peaks, rel_height = .99)[2],signal.peak_widths(abs(fft_sx)**2,peaks, rel_height = .99)[3]
print('Larghezze picchi: ', peaks_widths)
print('Larghezze picchi: ', left_peaks)
print('Larghezze picchi: ', right_peaks)

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
target_left_delim = left_peaks[target_freq_index]
target_right_delim = right_peaks[target_freq_index]

print(target_freq,target_freq_index, target_width)

#TODO left_ips

filter = [1 if ((i> abs(target_left_delim)) and i < abs(target_right_delim)) else 0 for i in freq]
# filter = [1 if i < abs(target_freq+target_width) else 0 for i in freq]

fft_filtered_signal = [fft_sx * filter,fft_dx * filter]

filtered_signal = [fft.irfft(i).real for i in fft_filtered_signal]
print(filtered_signal)
#writing new file with file audio

def write_audio_file(filename, samplerate, channel_data):
    # Normalizza ciascun canale audio dividendo per il massimo valore assoluto
    max_abs_values = [np.max(np.abs(channel)) for channel in channel_data]
    normalized_channels = [channel / max_abs_value for channel, max_abs_value in zip(channel_data, max_abs_values)]
    
    # Combina i dati dei canali in un array 2D
    audio_data = np.column_stack(normalized_channels)
    
    # Scalare i dati al range di valori consentiti per il formato wav int16
    
    # Scrivi il file wav utilizzando scipy.io.wavfile
    # write_wav(filename, samplerate, scaled_data)



# Scrivi il nuovo file audio normalizzato
# write_audio_file("filter.wav", fs, filtered_signal)
max_abs_values = [np.max(np.abs(channel)) for channel in filtered_signal]
normalized_channels = [channel / max_abs_value for channel, max_abs_value in zip(filtered_signal, max_abs_values)]
    
audio_data = np.column_stack(normalized_channels)
scaled_data = np.int16(audio_data * 32767)
sf.write('filter.wav',scaled_data, fs)

data2, fs2 = sf.read('filter.wav')
print("playing non-filtered data")
default_speaker.play(data=data/np.max(np.abs(data)), samplerate=fs)
time.sleep(.5)

print("playing filtered data")
default_speaker.play(data=data2/np.max(np.abs(data2)),samplerate=fs2)
# wf = wave.open("test.wav", 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(4)
# wf.setframerate(fs)
# wf.setnframes(int(fs * duration))
# wf.writeframes(filtered_signal[0])
# wf.close()
plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
plt.plot(t,channel_sx)
plt.ylabel("sound")
plt.xlabel("time(s)")

plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
plt.plot(freq,abs(fft_sx)**2)
plt.plot(freq[peaks],abs(fft_sx[peaks])**2, 'x')
plt.ylabel("")
plt.xlabel("frequency")
plt.title("potenza")

plt.figure(figsize=(16, 9))
plt.plot(freq,filter)
plt.ylabel("")
plt.xlabel("frequency")
plt.title("filter and filtered fft")


plt.figure(figsize=(16, 9))
plt.plot(t,filtered_signal[0])
plt.ylabel("")
plt.xlabel("time")
plt.title("Signal sx filtered")

plt.figure(figsize=(16, 9))
plt.plot(freq,abs(fft_filtered_signal[0])**2)
plt.ylabel("")
plt.xlabel("time")
plt.title("Signal sx filtered")



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
