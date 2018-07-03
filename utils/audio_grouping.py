## This script transfers all the spectrograms from the folder spectrograms 
## to the folder in tensorflow-for-poets-2/tf_files. 
## Inside tf_files, there are 9 folders with names from 0 to 9 
## so we move every specific spectrogram to the corresponding file.
## For example, all the spectrograms for number 0 are saved inside /tf_files/0.
## For number 1 inside /tf_files/1 etc.
import os
import shutil


srcpath = "/home/divinelink/Desktop/ASR-System/spectrograms"

files = os.listdir(srcpath)

for f in files:
    for i in range(0,10):
        destpath = "/home/divinelink/Desktop/ASR-System/tensorflow-for-poets-2/tf_files/spectrograms_photos/"+str(i)
        if f.startswith(str(i)):
            shutil.copy(srcpath+"/"+str(f), destpath)
