from pydub import AudioSegment
import os


def trim_audio(input_path, output_path, start_time, end_time):
    audio = AudioSegment.from_file(input_path)
    trimmed_audio = audio[(start_time * 1000):(end_time * 1000)]
    trimmed_audio.export(output_path, format="wav")


def ddd(arr, folder_path, file_path):
    returned = []
    unique_speakers = set()
    for i in range(len(arr)):
        unique_speakers.add(arr[i]['speaker'])

    for i in range(len(arr)):
        print(arr[i]['speaker'], i)
        speakers_path = f'{folder_path}/{arr[i]["speaker"]}'
        os.makedirs(speakers_path, exist_ok=True)
        trim_audio(file_path, f'{speakers_path}/{i}.wav', arr[i]['start'], arr[i]['stop'])
        returned.append({
            'start': arr[i]['start'],
            'stop': arr[i]['stop'],
            'speaker': f'{speakers_path}/full.wav'
        })
        print(arr[i])

    print(unique_speakers)
    for speaker in unique_speakers:
        filenames = os.listdir(f"{folder_path}/{speaker}")
        audios = AudioSegment.empty()
        for filename in filenames:
            audios += AudioSegment.from_file(f'{folder_path}/{speaker}/{filename}')
        audios.export(f'{folder_path}/{speaker}/full.wav', format="wav")

    return returned
