# Zyphra/Zonos

<div class="grid grid-cols-[50%_50%] gap-4" style="height: 85%;">
<!-- First Row -->
<div>
<ul>
<li>Open-weight TTS model</li>
<li>Phoneme, Pitch and Speaking Rate are adjustable</li>
<li>Voice cloning from 30s–5min voice samples</li>
</ul>
<div>

```python
model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device.type)

wav, sampling_rate = torchaudio.load(temp_input_path)
speaker = model.make_speaker_embedding(wav, sampling_rate)

cond_dict = make_cond_dict(text=text, speaker=speaker, language=language)
conditioning = model.prepare_conditioning(cond_dict)

codes = model.generate(conditioning)

wavs = model.autoencoder.decode(codes).cpu()
torchaudio.save(output_file_path, wavs[0], model.autoencoder.sampling_rate)
```

</div>
</div>
<div>
<LightOrDark>
<template #dark>
<img src="/MIINA.png" alt="girl screaming MIINA" class="object-contain"/>
</template>
<template #light>
<img src="/MIINA.png" alt="girl screaming MIINA" class="object-contain"/>
</template>
</LightOrDark>
</div>
</div>

<Footer />

<style>
p {
  margin-top: 0px;
  margin-bottom: 0px;
}

pre code {
  font-size: 0.75em;
}
</style>


<!-- What do I want to do on this slide: -->

<!-- As I heard about Zonos I immediatly had Vocaloids in my head... -->

<!-- Explanation on how they differ: -->
<!-- Vocaloid is for singing while Zonos can only do TTS -->
<!-- While it is possible to set rough phoneme directions with Zonos, the Vocaloid -->
<!-- Editors are far more capable in doing so. On the other side in Zonos you dont -->
<!-- need a database full of voice samples but only 30s - 5 mins of a voice sample -->
<!-- to get it speaking. -->

