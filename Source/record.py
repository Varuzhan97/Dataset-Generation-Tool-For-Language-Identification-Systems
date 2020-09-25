import pyaudio
import wave
import os
import string
import subprocess

class Recorder(object):
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024

    def rec(self, output_dir):
        while True:
            data_name = str(input('---| Enter Data (Language) Name ---> '))
            output_folder = os.path.join(output_dir, data_name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                break
            else:
                print('---| Data Name Exist |---', flush=True)
        data_name += ".wav"
        recording_filename = os.path.join(output_folder, data_name)
        self.start_recording(recording_filename)
        file_length_counter = self.get_dataset_length(recording_filename)
        print ("{} data total length: {:.2f} minutes.".format(data_name[:-4], file_length_counter))

    def start_recording(self, path):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk)
        print('---| Recording Started |---', flush=True)
        print('---| Press "CTRL + C" To Finish Recording |---', flush=True)
        frames = []
        try:
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        print('---| Recording Finished |---', flush=True)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wave_file = wave.open(os.path.join(os.path.dirname(path), os.path.basename(path)), 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(audio.get_sample_size(self.format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

    def get_dataset_length(self, target_dir):
        total = 0
        path = os.path.join(os.path.dirname(target_dir), os.path.basename(target_dir))
        command = "soxi -D \"%s\"" % path
        total += float(subprocess.check_output(command, shell=True))
        return (total/60)
