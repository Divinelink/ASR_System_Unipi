import os
import wave
import glob
import pylab
import matplotlib.pyplot as plt

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(8, 5))
    pylab.subplot(111)
    #pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig("/home/divinelink/Desktop/ASR-System/spectrograms/"+os.path.splitext(wav_file)[0]+'.png')
    plt.close()
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate


if __name__ == '__main__':
	for file in glob.glob("*.wav"):
		graph_spectrogram(file)
		
