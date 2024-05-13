import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal, fft
from scipy.signal import find_peaks,peak_widths
import soundfile as sf
import librosa


# aprire un piccolo file audio (.wav) e plottarne la waveform (solo un canale)
data, samplerate = sf.read('diapason.wav')

left_channel=data[:,0]
duration = len(left_channel) / samplerate

t = np.linspace(0,duration,len(left_channel))

# utilizzare l'array ottenuto dal file per creare un nuovo file audio (.wav), uguale al primo
sf.write('new_diapason.wav', data, samplerate)

#fare la FFT dell'array e plottare: potenza, parte reale e parte immaginaria dei coefficienti
fftaudio = fft.rfft(left_channel,norm="forward")

freq= fft.rfftfreq(len(left_channel),1/samplerate)

# aprire un piccolo file audio (.wav) e plottarne la waveform (solo un canale)
plt.title("Diapason")
plt.xlabel("Time")
plt.ylabel("Left Channel")
plt.legend()
plt.plot(t,left_channel)
plt.figure()

#Potenza
plt.title("Potenza")
plt.xlabel("Frequenza (hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.plot(freq,abs(fftaudio)**2, label="Abs")

#Picchi
peaks, _ = find_peaks(abs(fftaudio) ** 2, height=0.000028)
results_full = peak_widths(abs(fftaudio)**2, peaks, rel_height=0.99)
print(results_full[0])
plt.plot(freq[peaks],abs(fftaudio[peaks]) ** 2, "x")

#Note
note_number = librosa.hz_to_midi(freq[peaks])
note_name = librosa.midi_to_note(note_number)
print(note_name)
plt.figure()

#Reale
plt.title("Reale")
plt.plot(freq,fftaudio.real, label="Reale")
plt.figure()

#Immaginaria
plt.title("Imamginaria")
plt.plot(freq,fftaudio.imag, label="Imag")
plt.figure()

# Trova il picco principale
main_peak_index = np.argmax(abs(fftaudio) ** 2)
main_peak_freq = freq[main_peak_index]


plt.show()