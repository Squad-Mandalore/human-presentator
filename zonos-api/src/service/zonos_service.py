import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict
from zonos.utils import DEFAULT_DEVICE as device

from src.models.zonos_model import ZonosPostSchema

def create_zonos_model(zonos_schema: ZonosPostSchema) -> None:
    model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device.type)

    wav, sampling_rate = torchaudio.load(zonos_schema.audio_file_path)
    speaker = model.make_speaker_embedding(wav, sampling_rate)

    cond_dict = make_cond_dict(text=zonos_schema.text, speaker=speaker, language=zonos_schema.language)
    conditioning = model.prepare_conditioning(cond_dict)

    codes = model.generate(conditioning)

    wavs = model.autoencoder.decode(codes).cpu()
    torchaudio.save(zonos_schema.output_file_path, wavs[0], model.autoencoder.sampling_rate)

