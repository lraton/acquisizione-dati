import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq


# Esercizio 1:

sampleR = 1000       # Frequenza di campionamento
durata0 = 1          # Tempo di osservazione del segnale 
f0 = 5       # Frequenza
t = np.linspace(0,durata0,sampleR)       # Vettore tempo
xt = []                  # Array contenente i termini di Fourier
numeroCoeff = 10                   # Numero di coefficienti da utilizzare nella sommatoria

# Funzione che calcola i termini di Fourier
def calcola(t0):

    somma = 0
    
    for k in range(1,numeroCoeff):
        # Vogliamo solo i termini dispari
        if k % 2 == 1:
            somma = somma + (1/k*pow(-1, (k-1)/2)*np.cos(2*np.pi*k*f0*t0))
    
    return 1/2+2/np.pi*somma

for i in t:
    xt.append(calcola(i))

plt.figure()
plt.plot(t,xt)
plt.title("Segnale onda quadra")
plt.ylabel("x(t)")
plt.xlabel("Tempo (s)")


# Esercizio 2:

# Parte 1:

sampleRate1 = 1000  # Frequenza di campionamento
durata1 = 1  # Tempo di osservazione del segnale

t1 = np.linspace(0,durata1,sampleRate1,endpoint=False) # Vettore tempo  
f = [100,200,440]  # Insieme delle frequenze

# Per ogni frequenza in f si generano i segnali sinusoide, onda triangolare e onda quadra
# Inserisco ogni segnale all'interno della corrispettiva lista

ondasinusoidale = []
for freq in f:
    ondasinusoidale.append(np.sin(2*np.pi*freq*t1))

ondaquadra = []
for freq in f:
    ondaquadra.append(signal.square(2*np.pi*freq*t1))

ondatraingolare = []
for freq in f:
    ondatraingolare.append(signal.sawtooth(2*np.pi*freq*t1,0.5))  # il parametro 0.5 è stato inserito per ottenere una simmetria nella forma dell'onda


# Plot onda sinusoidale

plt.figure()
plt.xlabel("Tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondasinusoidale[0])
plt.title("Segnale onda sinusoidale")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondasinusoidale[1])
plt.title("Segnale: onda sinusoidale a 200 Hz")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondasinusoidale[2])
plt.title("Segnale: onda sinusoidale a 440 Hz")


# Plot onda triangolare

plt.figure()
plt.xlabel("Tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondatraingolare[0])
plt.title("Segnale onda triangolare")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondatraingolare[1])
plt.title("Segnale: onda triangolare a 200 Hz")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondatraingolare[2])
plt.title("Segnale: onda triangolare a 440 Hz") 


# Plot onda quadra

plt.figure()
plt.xlabel("Tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondaquadra[0])
plt.title("Segnale onda quadra")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondaquadra[1])
plt.title("Segnale: onda quadra a 200 Hz")

plt.figure()
plt.xlabel("tempo (s)")
plt.ylabel("x(t)")
plt.plot(t1, ondaquadra[2])
plt.title("Segnale: onda quadra a 440 Hz")



# Seconda parte:

# Effettuo la trasformata di Fourier di ogni onda e per ogni frequenza
# Calcolo le trasformate e le inserisco nella lista corrispondente

fftsinusoide = []
for onda in ondasinusoidale:
    fftsinusoide.append(fft(onda, norm='forward'))   # norm='forward' serve per la normalizzazione

fftquadra = []
for onda in ondaquadra:
    fftquadra.append(fft(onda, norm='forward'))
  
ffttraingolare = []
for onda in ondatraingolare:
    ffttraingolare.append(fft(onda, norm='forward'))


# Creazione vettore delle frequenze
freq = fftfreq(len(ondasinusoidale[0]), 1/sampleRate1)


# Plot per i segnali a 100 Hz

# Plot spettro di potenza dell'onda sinusoidale

plt.figure()
plt.plot(freq, abs(fftsinusoide[0])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: potenza")

# Plot parte immaginaria dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[0].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte immaginaria")

# Plot parte reale dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[0].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte reale")


# Plot spettro di potenza dell'onda quadra

plt.figure()
plt.plot(freq, abs(fftquadra[0])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: potenza")

# Plot parte immaginaria dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[0].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte immaginaria")

# Plot parte reale dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[0].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte reale")


# Plot spettro di potenza dell'onda triangolare

plt.figure()
plt.plot(freq, abs(ffttraingolare[0])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: potenza")

# Plot parte immaginaria dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[0].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte immaginaria")

# Plot parte reale dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[0].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte reale")



# Plot per i segnali a 200 Hz

# Plot spettro di potenza dell'onda sinusoidale

plt.figure()
plt.plot(freq, abs(fftsinusoide[1])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: potenza")

# Plot parte immaginaria dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[1].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte immaginaria")

# Plot parte reale dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[1].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte reale")


# Plot spettro di potenza dell'onda quadra

plt.figure()
plt.plot(freq, abs(fftquadra[1])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: potenza")

# Plot parte immaginaria dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[1].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte immaginaria")

# Plot parte reale dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[1].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte reale")


# Plot spettro di potenza dell'onda triangolare

plt.figure()
plt.plot(freq, abs(ffttraingolare[1])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: potenza")

# Plot parte immaginaria dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[1].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte immaginaria")

# Plot parte reale dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[1].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte reale")



# Plot per i segnali a 440 Hz

# Plot spettro di potenza dell'onda sinusoidale

plt.figure()
plt.plot(freq, abs(fftsinusoide[2])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: potenza")

# Plot parte immaginaria dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[2].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte immaginaria")

# Plot parte reale dell'onda sinusoidale

plt.figure()
plt.plot(freq, fftsinusoide[2].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda sinusoidale: parte reale")


# Plot spettro di potenza dell'onda quadra

plt.figure()
plt.plot(freq, abs(fftquadra[2])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: potenza")

# Plot parte immaginaria dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[2].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte immaginaria")

# Plot parte reale dell'onda quadra

plt.figure()
plt.plot(freq, fftquadra[2].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda quadra: parte reale")
plt.show()


# Plot spettro di potenza dell'onda triangolare

plt.figure()
plt.plot(freq, abs(ffttraingolare[2])**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: potenza")

# Plot parte immaginaria dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[2].imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte immaginaria")

# Plot parte reale dell'onda triangolare

plt.figure()
plt.plot(freq, ffttraingolare[2].real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Onda triangolare: parte reale")


# Terza parte:

segnaleSomma = ondasinusoidale[0] + ondasinusoidale[1] + ondasinusoidale[2]

fftSommaSinusoide = fft(segnaleSomma)

plt.figure()
plt.plot(freq, abs(fftSommaSinusoide)**2)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Segnale somma: potenza")

plt.figure()
plt.plot(freq, fftSommaSinusoide.imag)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Segnale somma: parte immaginaria")

plt.figure()
plt.plot(freq, fftSommaSinusoide.real)
plt.ylabel("$|X|_{k}$")
plt.xlabel("Frequenza (Hz)")
plt.title("Segnale somma: parte reale")

plt.show()
