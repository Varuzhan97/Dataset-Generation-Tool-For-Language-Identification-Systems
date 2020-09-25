import os
import glob
import string
import subprocess

class Segmenter(object):
    def __init__(self):
        self.input_path = os.path.join(os.getcwd(), "Recordings")
        if not os.path.exists(self.input_path):
            print('---| There Are No Recordings |---', flush=True)

    def clean_filename(self, filename):
        valid_chars = "-_%s%s" % (string.ascii_letters, string.digits)
        new_name = "".join(c for c in filename if c in valid_chars)
        new_name = new_name.replace(' ','_')
        return new_name

    def scan_dir(self, dirname):
        subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
        for dirname in list(subfolders):
            subfolders.extend(self.scan_dir(dirname))
        return subfolders

    def make_segment(self, input_dir, output_dir):

        folder_dir = self.scan_dir(input_dir)
        data_counter = 0
        labels = dict()
        for f in folder_dir:
            labels[os.path.basename(f)] = data_counter
            data_counter+=1
            file_dir = os.path.join(f, os.path.basename(f) + ".wav")
            print("---| Input File:  %s |---" %file_dir, flush=True)
            output_dir_segmented = os.path.join(output_dir, os.path.basename(f))
            if not os.path.exists(output_dir_segmented):
                os.makedirs(output_dir_segmented)
            cleaned_filename = self.clean_filename(os.path.basename(file_dir))
            cleaned_filename = cleaned_filename[:-3]
            output_filename = os.path.join(output_dir_segmented, cleaned_filename + "_%03d.wav")
            command = ["ffmpeg", "-y", "-i", file_dir, "-map", "0", "-ac", "1", "-ar", "16000", "-f", "segment", "-segment_time", "10", output_filename]
            subprocess.call(command, stderr=subprocess.DEVNULL)
            print("---| Generated |---", flush=True)
        return labels
