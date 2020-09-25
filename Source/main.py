from record import Recorder
from segment import Segmenter
from spectrogram import directory_to_spectrograms
from spectrogram import check_spectrograms
from csv_generator import create_csv
import os

if __name__ == '__main__':
    while True:
        output_record = os.path.join(os.getcwd(), "Recordings")
        output_segment = os.path.join(os.getcwd(), "Segmented Recordings")
        output_spectrogram = os.path.join(os.getcwd(), "Spectrograms")
        print("---| 0 -> Quit |---", flush=True)
        print("---| 1 -> Record |---", flush=True)
        print("---| 2 -> Generate Dataset |---", flush=True)
        x = int(input())
        if x == 0:
            break
        if x == 1:
            recorder = Recorder()
            recorder.rec(output_record)
        if x == 2:
            print("---| Segment Generation |---", flush=True)
            segmenter = Segmenter()
            labels = segmenter.make_segment(output_record, output_segment)
            create_csv(output_segment, labels)
            languages = list()
            for key in labels:
                languages.append(key)
            print("---| Spectrogram Generation |---", flush=True)
            directory_to_spectrograms(output_segment, output_spectrogram, languages)
            create_csv(output_spectrogram, labels)
            print("---| Spectrogram Checking |---", flush=True)
            check_spectrograms(output_spectrogram)
