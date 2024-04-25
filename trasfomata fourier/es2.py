import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal, fft

sampling_rate=1000
t = np.linspace(0, 1, sampling_rate, endpoint=False)

frequencies = [100, 200, 440]  # Frequenze in Hz

w1 = [np.sin(2 * np.pi * f * t) for f in frequencies]
w2 = [signal.square(2 * np.pi * f * t) for f in frequencies]
w3 = [signal.sawtooth(2 * np.pi * f * t,0.45) for f in frequencies]

fft1 = [fft.fft(i) for i in w1]
fft2 = [fft.fft(i) for i in w2]
fft3 = [fft.fft(i) for i in w3]

freq= fft.fftfreq(len(w1[0]),1/sampling_rate)

plt.title("Onde Sinusoidali a Diverse Frequenze")
plt.plot(freq,abs(fft1[0])**2, label="Abs 100 Hz")

plt.figure()
plt.plot(freq,abs(fft1[1])**2, label="Abs 200 Hz")

plt.figure()
plt.plot(freq,abs(fft1[2])**2, label="Abs 440 Hz")
plt.figure()
plt.plot(freq,fft1[0].real, label="Reale 100 Hz")
plt.figure()
plt.plot(freq,fft1[1].real, label="Reale 200 Hz")
plt.figure()
plt.plot(freq,fft1[2].real, label="Reale 440 Hz")
plt.figure()
plt.plot(freq,fft1[0].imag, label="Imag 100 Hz")
plt.figure()
plt.plot(freq,fft1[1].imag, label="Imag 200 Hz")
plt.figure()
plt.plot(freq,fft1[2].imag, label="Imag 440 Hz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.figure()

plt.title("Onde Quadre a Diverse Frequenze")
plt.plot(freq,abs(fft2[0])**2, label="100 Hz")
plt.plot(freq,abs(fft2[1])**2, label="200 Hz")
plt.plot(freq,abs(fft2[2])**2, label="4400 Hz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.figure()

plt.title("Onde triangolari a Diverse Frequenze")
plt.plot(freq,abs(fft3[0])**2, label="100 Hz")
plt.plot(freq,abs(fft3[1])**2, label="200 Hz")
plt.plot(freq,abs(fft3[2])**2, label="440 Hz")


plt.xlabel("Frequenza (hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()