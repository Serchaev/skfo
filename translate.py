from transformers import pipeline


def translate(lang: str, text: str = None, segments: list = None):
    pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")
    if not segments:
        res = pipe(text, src_lang="rus_Cyrl", tgt_lang=lang)
        return res[0]['translation_text']
    else:
        my_segments = []
        for segment in segments:
            res = pipe(segment.text, src_lang="rus_Cyrl", tgt_lang=lang)
            my_segments.append({
                "start": segment.start,
                "end": segment.end,
                "text": res[0]['translation_text'],
            })
        return my_segments

# translate()
