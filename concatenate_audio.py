import os
from pydub import AudioSegment


def concatenate_audio(folder_path, output_audio_path, start_timing=0):
    file_count = len(os.listdir(folder_path))
    output = None

    for i in range(file_count):
        audio = AudioSegment.from_wav(f"{folder_path}/outputSegment_{i}.wav")
        print(audio.duration_seconds)

        if output is None:
            output = AudioSegment.silent(duration=start_timing*1000) + audio
        else:
            output = output.append(audio, crossfade=100)

    output.export(output_audio_path)


# concatenate_audio("work/65/segments", "work/65/segments/output.wav")
