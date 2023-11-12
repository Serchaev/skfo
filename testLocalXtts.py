from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

config = XttsConfig()
config.load_json("models/xtts/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="models/xtts/", eval=True)
model.cuda()

outputs = model.synthesize(
    "I think you have a lot of questions, so get ready and do not hesitate to ask them.",
    config,
    speaker_wav="my/cloning/audio2_Vocals.wav",
    gpt_cond_len=6,
    language="ru",
)
