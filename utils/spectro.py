import os
import wave
import glob
import pylab
import cv2



def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(8,5))
    pylab.subplot(111)
    pylab.specgram(sound_info, Fs=frame_rate)    
    pylab.savefig(os.path.splitext(wav_file)[0]+'.png')

    #Crop image border, so it doesn't have number details about frequency and time. 
    #We don't need that kind of data for our training.
    img = cv2.imread(os.path.splitext(wav_file)[0]+'.png')
    cropped_img = img[60:446, 100:721]
    cv2.imwrite(os.path.splitext(wav_file)[0]+'.png', cropped_img)
   


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
		
