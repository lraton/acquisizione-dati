import numpy as np
import soundcard as sc
import matplotlib.pyplot as plt 

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()

print(default_speaker)
print(default_mic)

# record and play back one second of audio:
data = default_mic.record(samplerate=48000, numframes=480000)

# normalized playback
default_speaker.play(data/np.max(np.abs(data)), samplerate=48000)

# Half the speed
default_speaker.play(data/np.max(np.abs(data)), samplerate=48000*2)

# Double the speed
default_speaker.play(data/np.max(np.abs(data)), samplerate=int(48000/2))

#plot one chanel of the audio

print(data) # Print the data

plt.plot(data) # Plotting all the wave

plt.figure(figsize=(10,6))
num_channels = data.shape[1]
for i in range(num_channels):
    plt.plot(np.linspace(0, 10, len(data)), data[:, i], label=f'Channel {i+1}') #Plotting the channel separate


plt.title('Audio')
plt.xlabel('Time samples')
plt.ylabel('Amplitude')
plt.show()
