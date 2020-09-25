import os
import argparse
import imageio
import numpy as np
import sys
import glob
import csv
from spectrogram_generator import SpectrogramGenerator
from noisy_background_spectrogram_generator import NoisyBackgroundSpectrogramGenerator

def check_spectrograms(csv_dir):
    csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))
    for f in csv_files:
        print("---| Detected: %s |---" % os.path.basename(f), flush=True)
        with open(f, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            output_dir = os.path.dirname(f)
            output_dir = os.path.join(output_dir, "temp_" + os.path.basename(f))
            output = open(output_dir, 'w')
            writer = csv.writer(output)
            for row in reader:
                image_path, label = row
                image = imageio.imread(image_path, pilmode="L")
                if(np.count_nonzero(image-np.mean(image)) == 0):
                    print("---| Removing: %s |---" % image_path, flush=True)
                else:
                    writer.writerow(row)
            os.remove(f)
            rename_path = os.path.join(os.path.dirname(f), os.path.basename(f))
            os.rename(output_dir, rename_path)


def directory_to_spectrograms(source, target, languages):

    config = {
        "pixel_per_second": 50,
        "input_shape": [129, 500, 1]
    }
    print("---| 1 -> Enable Noise Filter |---", flush=True)
    print("---| 0 -> Disable Noise Filter |---", flush=True)
    x = int(input())
    if x==1:
        generators = [NoisyBackgroundSpectrogramGenerator(os.path.join(source, language), config, shuffle=False, run_only_once=True) for language in languages]
    else:
        generators = [SpectrogramGenerator(os.path.join(source, language), config, shuffle=False, run_only_once=True) for language in languages]
    generator_queues = [SpectrogramGen.get_generator() for SpectrogramGen in generators]
    for language in languages:
        output_dir = os.path.join(target, language)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    i = 0
    while True:
        target_shape = tuple([129, 500, 1])
        try:
            for j, language in enumerate(languages):
                data = next(generator_queues[j])
                assert data.shape == target_shape, "Shape mismatch {} vs {}".format(data.shape, [129, 500, 1])
                file_name = os.path.join(target, language, "{}.png".format(i))
                imageio.imwrite(file_name, np.squeeze(data))
            i += 1
        except StopIteration:
            print("---| Saved {} Images |---".format(i))
            break
