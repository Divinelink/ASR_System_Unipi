import pyaudio, wave
from pydub import AudioSegment
from pydub.silence import split_on_silence
import pylab, cv2
import sys, os
from ctypes import *
sys.path.append(os.path.abspath("/home/divinelink/Desktop/ASR-System/tensorflow-for-poets-2/scripts"))

from label_image import show_results



## NEEDED FOR SPECTROGRAM ##
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

    # evaluate which number the user said.
    # This method is imported from tensorflow-for-poets2 folder.
    #read_tensor_from_image_file(cropped_img)
    show_results(os.path.splitext(wav_file)[0]+'.png')

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
## END ##

## SPLIT AUDIO FILE TO CHUNKS ##
def split_audio(wav_file):
	sound_file = AudioSegment.from_wav(wav_file)
	audio_chunks = split_on_silence(sound_file,
	    # must be silent for at least half a second
	    min_silence_len=500,

	    # consider it silent if quieter than -16 dBFS
	    silence_thresh=-25
	)

	for i, chunk in enumerate(audio_chunks):

	    out_file = "./number{0}.wav".format(i)
	    #print "exporting", out_file
            chunk.export(out_file, format="wav")
	    #print "graphing spectrogram"
            graph_spectrogram(out_file)

## END ##

## RECORD USER'S VOICE ##

def record_audio():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 8000
	RECORD_SECONDS = 10
	WAVE_OUTPUT_FILENAME = "usersRecord.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
		        channels=CHANNELS,
		        rate=RATE,
		        input=True,
		        frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	#Split audio into chucks using split_audio method
	split_audio(WAVE_OUTPUT_FILENAME)
## END ##

if __name__ == '__main__':
	record_audio()
