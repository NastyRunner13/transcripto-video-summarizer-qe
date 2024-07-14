from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

def wav2vec2model():
    model_name = "facebook/wav2vec2-base-960h"
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    return model, processor