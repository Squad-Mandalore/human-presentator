import torch
import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict
from zonos.utils import DEFAULT_DEVICE as device

def main():
    # model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-hybrid", device=device)
    model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device.type)

    wav, sampling_rate = torchaudio.load("assets/exampleaudio.mp3")
    speaker = model.make_speaker_embedding(wav, sampling_rate)

    cond_dict = make_cond_dict(text="Hallo Welt!", speaker=speaker, language="de")
    conditioning = model.prepare_conditioning(cond_dict)

    codes = model.generate(conditioning)

    wavs = model.autoencoder.decode(codes).cpu()
    torchaudio.save("sample.wav", wavs[0], model.autoencoder.sampling_rate)


if __name__ == "__main__":
    main()
