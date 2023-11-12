import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
# print(device)
# List available 🐸TTS models
# print(TTS().list_models())

tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24").to(device)
tts.voice_conversion_to_file(source_wav="my/source.wav", target_wav="my/target.wav", file_path="output1.wav")
