# load the pipeline from Hugginface Hub
import time
import torchaudio

from pyannote.audio import Pipeline
import torch
# a = time.time()


def diarization(path: str) -> list:
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.0", use_auth_token="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")

    pipeline.to(torch.device("cuda"))

    # apply the pipeline to an audio file
    # diarization = pipeline("audio4.wav")
    waveform, sample_rate = torchaudio.load(path)
    diarization1 = pipeline({"waveform": waveform, "sample_rate": sample_rate}, num_speakers=1)

    # hparams = pipeline.parameters(instantiated=True)
    # hparams["clustering"]["threshold"] += 0.1
    # pipeline.instantiate(hparams)
    # print(hparams)


    # dump the diarization output to disk using RTTM format
    # with open("audio4.rttm", "w") as rttm:
    #     diarization.write_rttm(rttm)

    # print the result
    lst = []
    for turn, _, speaker in diarization1.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        if len(lst) > 0 and lst[-1]["speaker"] == speaker:
            lst[-1]["stop"] = turn.end

        elif turn.end - turn.start > 1.0 and len(lst) > 0:
            lst.append({
                "start": lst[-1]["stop"] + 0.01,
                "stop": turn.end,
                "speaker": speaker,
            })

        elif turn.end - turn.start > 1.0:
            lst.append({
                "start": turn.start,
                "stop": turn.end,
                "speaker": speaker,
            })

    return lst

# b = time.time()
# print(b-a)
