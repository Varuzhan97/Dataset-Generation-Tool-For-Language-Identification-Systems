# Dataset-Generation-Tool-For-Language-Identification-Systems
Dataset Generation Tool For Language Identification Systems That Use Deep Convolutional Recurrent Neural Networks.

## Description 
Datasets are an integral part of the field of machine learning. The tool can generate a human-labelled dataset from the environment(both noisy and clear)  for [language identification (LID) systems that use deep convolutional recurrent neural networks (CRNN)](https://arxiv.org/pdf/1708.04811.pdf).
The system takes the recording received from a microphone and has a ".wav" extension. The next step is to make segments with 10 seconds duration from the recording. After that system generates spectrograms form segments and checks for bad images. The final results are spectrogram images dataset containing description files for training, validation and testing parts of the dataset.  Description files have ".csv" extension and contain the links of the spectrograms in the local memory and their corresponding indexes(label of data name). The steps described are shown in figure below.


![alt text](https://github.com/Varuzhan97/Dataset-Generation-Tool-For-Language-Identification-Systems/blob/master/Structure%20Of%20The%20System/structure.png?raw=true)


Configurations for recording:
1. Sampling size is 16 bit integer format.
2. Channels number is 1.
3. Sampling rate is 44100 Hz.
4. The number of frames per buffer is 1024.

The spectrogram generation process can be done in two ways: 
1. Generation from a noisy environment.
2. Generation from a clear environment.

Configurations for generating spectrograms from noisy and/or clear environments:
1. Spectrogram image contains 50 pixel per second.
2. Spectrogram image is 129x500.
3. Channels number is 1.
4. Channel is mono. 
5. Rate is 10k.

The creation of spectrograms is followed by the process of checking bad spectrograms. The steps are as follows: 
1. The image becomes a vector of the sequence of pixel values .
2. The arithmetic mean of the pixel values is calculated.
3. The arithmetic mean of the pixel values calculated in the previous step is subtracted from each pixel value of the image.
4. The image is removed from the dataset if the number of non-zero elements in the vector obtained by subtraction is equal to zero.

## Install Python 3 Requirements
*pip3 install -r requirements.txt*

## Run
*python3 main.py*





