#!/home/leonardo/Programs/python_env/bin/python3

import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal,fft
import numpy as np
import librosa, time
import wave
import soundcard as sc


class Filter():

    def __init__(self, freq, lb, rb) -> None:
        self.freq = freq
        self.lb = lb
        self.rb = rb
        self.signal = [1 if ((i> abs(freq[int(self.lb)])) and i < abs(freq[int(self.rb)])) else 0 for i in self.freq] 
             

# get the current default speaker on your system:
default_speaker = sc.default_speaker()

#read file and get duration
path_to_audio = ['diapason.wav','pulita_semplice.wav','distorta.wav']
selected_audio = path_to_audio[1]
data, fs = sf.read(selected_audio)
f = sf.SoundFile(selected_audio)
duration = f.frames/f.samplerate


#write new audio file
sf.write('new_diapason.wav',data,fs)

#select channel, get fft and plot all
channel_sx = data[:,0]
channel_dx = data[:,1]
freq = fft.rfftfreq(len(channel_sx),1./fs)
t = np.linspace(0,duration,len(channel_sx))
fft_sx = fft.rfft(channel_sx,norm='forward')
fft_dx = fft.rfft(channel_dx,norm='forward')
ffts = [fft_sx,fft_dx]
#find peak and peaks width

peaks = [signal.find_peaks(abs(i)**2, height = 2.8e-5, rel_height = .99)[0] for i in ffts]
peak_heights = [signal.find_peaks(abs(i)**2, height = 2.8e-5, rel_height = .99)[1]['peak_heights'] for i in ffts]
print('Picchi: ',peaks, 'Numero Picchi: ', len(peaks))
print('Peak heights: ', peak_heights)


peaks_widths = [signal.peak_widths(abs(i)**2,j, rel_height = .99)[0] for i,j in zip(ffts, peaks)]
left_peaks , right_peaks = [signal.peak_widths(abs(i)**2,j, rel_height = .99)[2] for i,j in zip(ffts, peaks)],\
[signal.peak_widths(abs(i)**2,j, rel_height = .99)[3] for i,j in zip(ffts, peaks)]
print('Larghezze picchi: ', peaks_widths)
print('Margine sinistro picchi: ', left_peaks)
print('Margine destro picchi: ', right_peaks)

#convert peak frequencies to musical notes
notes = [librosa.hz_to_note(freq[i]) for i in peaks]
print('Note corrispondenti ai picchi: ',notes)

#filter main peak and write new file audio
target_freq_index = [np.argmax(i) for i in peak_heights]
target_left_delim =[]
target_right_delim =[]

for i in range(2):
    target_width = peak_heights[i][target_freq_index[i]]
    target_left_delim.append(left_peaks[i][target_freq_index[i]])
    target_right_delim.append(right_peaks[i][target_freq_index[i]])

filters = [Filter(freq,i,j) for i,j in zip(target_left_delim,target_right_delim)]
# filter = [[1 if ((i> abs(freq[int(target_left_delim[])])) and i < abs(freq[int(target_right_delim)])) else 0 for i in freq] for j in range(2)]
# filter = [1 if i < abs(freq[int(target_right_delim)]) else 0 for i in freq] #passa basso

#applying the filter
fft_filtered_signal = [i*j.signal for i,j in zip(ffts, filters)]
filtered_signal = [fft.irfft(i).real for i in fft_filtered_signal]

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

plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
plt.plot(t,channel_sx)
plt.ylabel("sound")
plt.xlabel("time(s)")

plt.figure(figsize=(16, 9))  # Set the figure size to 8 inches wide and 6 inches tall
plt.plot(freq,abs(fft_sx)**2)
plt.plot(freq[peaks[0]],abs(fft_sx[peaks[0]])**2, 'x')
plt.ylabel("")
plt.xlabel("frequency")
plt.title("potenza")

plt.figure(figsize=(16, 9))
plt.plot(freq,filters[0].signal)
plt.ylabel("")
plt.xlabel("frequency")
plt.title("filter")

plt.figure(figsize=(16, 9))
plt.plot(t,filtered_signal[0])
plt.ylabel("")
plt.xlabel("time(s)")
plt.title("Signal sx filtered")

plt.figure(figsize=(16, 9))
plt.plot(freq,abs(fft_filtered_signal[0])**2)
plt.ylabel("")
plt.xlabel("frequency")
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