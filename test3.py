from pydub import AudioSegment
import numpy
from scipy.io import wavfile


def remove_silence(audio, threshold):
    greater_index = numpy.greater(numpy.absolute(audio), threshold)
    above_threshold_data = audio[greater_index]
    return above_threshold_data


def change_audio(audio_path, output_path, seconds):
    threshold = 110
    sotu_rate, sotu_data = wavfile.read(audio_path)
    sotu_above_threshold = remove_silence(sotu_data, threshold)
    wavfile.write(output_path, sotu_rate, sotu_above_threshold)
    if AudioSegment.from_file(audio_path).duration_seconds < seconds:
        differ = seconds - AudioSegment.from_file(audio_path).duration_seconds
        asd = AudioSegment.from_file(audio_path) + AudioSegment.silent(duration=differ*1000)
        asd.export(output_path, format="wav")