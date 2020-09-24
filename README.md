# Dataset-Generation-Tool-For-Language-Identification-Systems
Dataset Generation Tool For Language Identification Systems That Use Deep Convolutional Recurrent Neural Networks.

Datasets are an integral part of the field of machine learning. The tool that can generate a human-labelled dataset from the environment(both noisy and clear)  for [language identification (LID) systems that use deep convolutional recurrent neural networks (CRNN)](https://arxiv.org/pdf/1708.04811.pdf).

This is a brief description of how the system works: the system takes the recording received from a microphone and has a ".wav" extension. The next step is to make segments with 10 seconds duration from the recording. After that system generates spectrograms form segments and checks for bad images. The final results are spectrogram images dataset containing description files for training, validation and testing parts of the dataset.  Description files have ".csv" extension and contain the links of the spectrograms in the local memory and their corresponding indexes(label of data name). The steps described are shown in figure below.

![alt text](https://github.com/Varuzhan97/Dataset-Generation-Tool-For-Language-Identification-Systems/blob/master/Structure%20Of%20The%20System/structure.png?raw=true)



