# Dataset-Generation-Tool-For-Language-Identification-Systems
Dataset Generation Tool For Language Identification Systems That Use Deep Convolutional Recurrent Neural Networks.

This is a brief description of how the system works: the system takes the recording received from a microphone and has a ".wav" extension. The next step is to make segments with 10 seconds duration from the recording. After that system generates spectrograms form segments and checks for bad images. The final results are spectrogram images dataset containing description files for training, validation and testing parts of the dataset.  Description files have ".csv" extension and contain the links of the spectrograms in the local memory and their corresponding indexes(label of data name). The steps described are shown in figure below.
![alt text](https://github.com/Varuzhan97/Dataset-Generation-Tool-For-Language-Identification-Systems/blob/master/Structure%20Of%20The%20System/structure.png?raw=true)
Configurations for recording:
    Sampling size is 16 bit integer format.
    Channels number is 1.
    Sampling rate is 44100 Hz.
The number of frames per buffer is 1024.
The process of splitting the input data  after segmentation is done in the following stages:
Determine the minimum number of data segments (after this: smallest) in all data.
Test files (after this: test) are determined by the following formula:  smallest  *  0.05.
Training files (after this: train) are determined by the following formula:  smallest * (0.8 - 0.05). 0.8 is the train set and validation set split.
Validation files are determined by the following formula:  smallest - train - test.
The spectrogram generation process can be done in two ways: 
Generation from a noisy environment.
Generation from a clear environment. 
Configurations for generating spectrograms from noisy and/or clear environments:
Spectrogram image contains 50 pixel per second.
Spectrogram image is 129x500.
Channels number is 1.
Channel is mono. 
Rate is 10k[3].
The creation of spectrograms is followed by the process of checking bad spectrograms. The steps are as follows: 
The image becomes a vector of the sequence of pixel values .
The arithmetic mean of the pixel values is calculated.
The arithmetic mean of the pixel values calculated in the previous step is subtracted from each pixel value of the image.
The image is removed from the dataset if the number of non-zero elements in the vector obtained by subtraction is equal to zero.

