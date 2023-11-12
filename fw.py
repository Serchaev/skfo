from faster_whisper import WhisperModel


def fw(path: str) -> list:

    model_size = "large-v2"

    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    segments, info = model.transcribe(
        path,
        beam_size=5,
        language="ru",
        # task="translate",
        vad_filter=True,
        # word_timestamps=True,
    )

    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    # print()
    # print(info)
    # print()

    # for segment in segments:
    #     # print(segment)
    #     # print()
    #     # print()
    #     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    segments = list(segments)
    return segments
