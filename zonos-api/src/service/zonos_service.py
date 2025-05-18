import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict
from zonos.utils import DEFAULT_DEVICE as device


def generate_zonos_audio(temp_input_path: str, text: str, language: str, output_file_path: str) -> None:
    model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device.type)

    wav, sampling_rate = torchaudio.load(temp_input_path)
    speaker = model.make_speaker_embedding(wav, sampling_rate)

    cond_dict = make_cond_dict(text=text, speaker=speaker, language=language)
    conditioning = model.prepare_conditioning(cond_dict)

    codes = model.generate(conditioning)

    wavs = model.autoencoder.decode(codes).cpu()
    torchaudio.save(output_file_path, wavs[0], model.autoencoder.sampling_rate)

