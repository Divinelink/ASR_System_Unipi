## This bash script creates the spectrogram from a given .wav file
## --#1 In order to run this script you should first give change the permission 
## using chmod 755 spectrogramer.sh on a terminal
## --#2 Lastly you have to move this file to the folder that your .wav files belong. 
## In this case I ran the script on the /audiofiles folder
## and it saved the corresponding images on the /spectrograms folder.

for w in *.wav
do
    name=$(echo "$w" | cut -f 1 -d '.')
    sox "$w" -n spectrogram -o "/home/divinelink/Desktop/ASR-System/spectrograms/$name.png"
done
