import json
import os

from nemo.collections.asr.models import ClusteringDiarizer
from omegaconf import OmegaConf
#
# INPUT_FILE = '/PATH/TO/AUDIO_FILE.wav'
# MANIFEST_FILE = '/PATH/TO/MANIFEST_FILE.json'
#
# meta = {
#     'audio_filepath': input_file,
#     'offset': 0,
#     'duration': None,
#     'label': 'infer',
#     'text': '-',
#     'num_speakers': None,
#     'rttm_filepath': None,
#     'uem_filepath': None
# }
# with open(MANIFEST_FILE, 'w') as fp:
#     json.dump(meta, fp)
#     fp.write('\n')