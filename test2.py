from pydub import AudioSegment
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter
from pydub import AudioSegment


def speed_up_audio(input_path, output_path, speed):
    audio = AudioSegment.from_file(input_path, 'wav')
    new_audio = audio.speedup(playback_speed=speed)
    new_audio.export(output_path, format="mp3")


def speed_down_audio(input_audio_path, output_audio_path, speed):
    with WavReader(input_audio_path) as reader:
        with WavWriter(output_audio_path, reader.channels, reader.samplerate) as writer:
            tsm = phasevocoder(reader.channels, speed=speed)
            tsm.run(reader, writer)

# def speed_change(sound, speed=1.0):
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
#         "frame_rate": int(sound.frame_rate * speed)
#     })
#     return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


def change_audio_duration(audio_path, target_duration):
    audio = AudioSegment.from_wav(audio_path)

    current_duration = len(audio)
    print(len(audio))
    print(target_duration)
    if current_duration > target_duration:
        speedup_ratio = current_duration / target_duration
        # audio = audio.speedup(playback_speed=speedup_ratio)
        speed_up_audio(input_path=audio_path, output_path=f"{audio_path[:-4]}2.wav", speed=speedup_ratio)

    elif current_duration < target_duration:
        speedup_ratio = current_duration / target_duration
        slowdown_ratio = target_duration / current_duration
        print(speedup_ratio)
        print(slowdown_ratio)
        print(1 / slowdown_ratio)

        # audio = audio.speedup(playback_speed=slowdown_ratio)
        # speed_change(audio, 1 / slowdown_ratio)
        speed_down_audio(input_audio_path=audio_path, output_audio_path=f"{audio_path[:-4]}2.wav", speed=1 / slowdown_ratio)
    # audio.export(f"{audio_path[:-4]}2.wav")
