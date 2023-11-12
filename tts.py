import torch
from TTS.api import TTS


def ttf(text: str, output: str, segments: list = None, idv: str = None, diar: list = None):

    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    if segments:
        for index, segment in enumerate(segments):
            speaker_path = ""

            for i in diar:
                if (i["start"] <= segment["start"] < i["stop"]) or (i["start"] < segment["end"] <= i["stop"]):
                    speaker_path = f"{i['speaker']}"

            path = f"work/{idv}/segments/outputSegment_{index}.wav"
            tts.tts_to_file(
                text=segment["text"],
                speaker_wav=speaker_path,
                language="en",
                file_path=path
            )

    else:
        tts.tts_to_file(
            text=text,
            speaker_wav="my/cloning/audio2_Vocals.wav",
            language="en",
            file_path=output
        )
