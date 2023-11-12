import time

from add_audio_to_video import add_audio
from concatenate_audio import concatenate_audio
from ddd import ddd
from diarization import diarization
from extract_audio import extract_audio
from fw import fw
from test2 import change_audio_duration
from test3 import change_audio
from translate import translate
from tts import ttf
import subprocess


def main(path: str, idv: str, lang: str):
    print(path, idv, lang)

    extract_audio(video_path=path, audio_path=f"my/cloning/audio2.wav")
    command = 'python inference.py --input ../my/cloning/audio2.wav --tta --gpu 0 --output_dir ../my/cloning'
    subprocess.run(command.split(), cwd='vocal-remover')

    segments = fw("my/cloning/audio2_Vocals.wav")
    # segments = fw(path)
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

    my_segments = translate(lang=lang, segments=segments)
    # my_segments[0]["start"] = 5.2

    diarizer = diarization("my/cloning/audio2_Vocals.wav")
    print(diarizer)
    # diarizer[0]["start"] = 18.80
    my_segments[0]["start"] = diarizer[0]["start"]

    diarizer2 = ddd(diarizer, f"work/{idv}", "my/cloning/audio2_Vocals.wav")


    print(my_segments)
    text = ""
    text2 = ""
    for segment in my_segments:
        text += "[%.2fs -> %.2fs] %s \n" % (segment["start"], segment["end"], segment["text"])
        text2 += segment["text"]
        # my_segments.append({
        #     "start": segment.start,
        #     "end": segment.end,
        #     "text": translate(text=segment.text, lang=lang),
        # })

        # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

    # with open(f"work/{idv}/1{idv}.txt", "w", encoding="utf-8") as file:
    #     file.write(text)
    #
    # # for index, segment in enumerate(segments):
    #     path = f"output/outputSegment_{index}.wav"
    # ttf(text2, "./output.wav")

    ttf(text2, "./output3.wav", my_segments, idv, diarizer2)
    for index, segment in enumerate(my_segments):
        path2 = f"work/{idv}/segments/outputSegment_{index}.wav"
        # change_audio_duration(audio_path=path, target_duration=(segment.end-segment.start)*1000)
        change_audio(audio_path=path2, output_path=f"work/{idv}/segments/outputSegment_{index}.wav",
                     seconds=segment["end"] - segment["start"])
    #
    #
    concatenate_audio(f"work/{idv}/segments", f"work/{idv}/segments/output.wav", my_segments[0]["start"])
    #
    add_audio(video_path=path, audio1_path=f"work/{idv}/segments/output.wav",
              audio2_path="my/cloning/audio2_Instruments.wav", output_path=f"{idv}.mp4")


if __name__ == "__main__":
    import os

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    a = time.time()
    main(path="dataset/12.mp4", idv="12", lang="eng_Latn")
    # langs = ['deu_Latn', 'eng_Latn', 'fra_Latn', 'ita_Latn', 'spa_Latn', 'eng_Latn', 'jpn_Jpan', 'eng_Latn', 'ita_Latn',
    #          'zho_Hans',
    #          'eng_Latn', 'fra_Latn', 'eng_Latn', 'eng_Latn', 'deu_Latn', 'fra_Latn', 'zho_Hans', 'eng_Latn', 'eng_Latn',
    #          'jpn_Jpan',
    #          'deu_Latn', 'eng_Latn', 'fra_Latn', 'ita_Latn', 'spa_Latn', 'eng_Latn', 'jpn_Jpan', 'eng_Latn', 'ita_Latn',
    #          'zho_Hans',
    #          'eng_Latn', 'ita_Latn', 'spa_Latn', 'deu_Latn', 'jpn_Jpan', 'por_Latn', 'jpn_Jpan', 'zho_Hans', 'ces_Latn',
    #          'dan_Latn',
    #          'pol_Latn', 'tur_Latn', 'eng_Latn', 'eng_Latn', 'eng_Latn', 'eng_Latn', 'fra_Latn', 'ita_Latn', 'eng_Latn',
    #          'jpn_Jpan',
    #          'eng_Latn', 'ita_Latn', 'zho_Hans', 'jpn_Jpan', 'por_Latn', 'jpn_Jpan', 'zho_Hans', 'ces_Latn', 'dan_Latn',
    #          'pol_Latn',
    #          'tur_Latn', 'eng_Latn', 'eng_Latn', 'eng_Latn', 'eng_Latn', 'deu_Latn', 'eng_Latn', 'fra_Latn', 'ita_Latn',
    #          'spa_Latn',
    #          'eng_Latn', 'jpn_Jpan', 'eng_Latn', 'ita_Latn', 'zho_Hans', 'eng_Latn', 'fra_Latn', 'eng_Latn', 'eng_Latn',
    #          'deu_Latn',
    #          'fra_Latn', 'zho_Hans', 'eng_Latn', 'eng_Latn', 'deu_Latn', 'deu_Latn', 'eng_Latn', 'fra_Latn', 'ita_Latn',
    #          'spa_Latn',
    #          'eng_Latn', 'jpn_Jpan', 'eng_Latn', 'ita_Latn', 'zho_Hans', 'eng_Latn', 'fra_Latn', 'eng_Latn', 'deu_Latn',
    #          'fra_Latn']
    # for index, val in enumerate(langs):
    #     main(path=f"dataset/{index}.mp4", idv=index, lang=val)
    print(time.time() - a)
