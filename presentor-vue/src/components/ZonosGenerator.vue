<template>
  <div class="p-6 border rounded-lg shadow-lg space-y-4">
    <h2 class="text-2xl font-semibold">1. Generate Speech</h2>

    <!-- Recording controls -->
    <div class="space-x-2">
      <button
        class="px-4 py-2 bg-red-600 text-white rounded"
        @click="startRecording"
        :disabled="recording"
      >Start Recording Sample</button>
      <button
        class="px-4 py-2 bg-gray-300 rounded"
        @click="stopRecording"
        :disabled="!recording"
      >Stop</button>
      <span v-if="recording" class="text-red-500 font-medium">● Recording…</span>
    </div>

    <!-- Preview recorded sample -->
    <audio
      v-if="sampleUrl"
      :src="sampleUrl"
      controls
      class="w-full"
    ></audio>

    <!-- Text & language inputs -->
    <div class="flex flex-col space-y-2">
      <input
        v-model="text"
        type="text"
        placeholder="Text to speak…"
        class="border p-2 rounded"
      />
      <input
        v-model="language"
        type="text"
        placeholder="Language (e.g. en-us)"
        class="border p-2 rounded"
      />
    </div>

    <button
      class="mt-2 w-full py-2 bg-blue-600 text-white rounded"
      @click="generateSpeech"
      :disabled="!sampleBlob || !text || !language || loading"
    >
      {{ loading ? 'Generating…' : 'Generate Speech' }}
    </button>

    <!-- Playback & download of generated audio -->
    <div v-if="audioUrl" class="space-y-2">
      <audio :src="audioUrl" controls class="w-full"></audio>
      <a
        :href="audioUrl"
        download="zonos-output.wav"
        class="inline-block mt-1 px-4 py-2 bg-green-600 text-white rounded"
      >Download WAV</a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

/** ——— State with explicit types ——— **/
const recording      = ref<boolean>(false)
const recorder       = ref<MediaRecorder|null>(null)
const chunks         = ref<Blob[]>([])
const sampleBlob     = ref<Blob|null>(null)
const sampleUrl      = ref<string|null>(null)

const text           = ref<string>('')
const language       = ref<string>('en-us')
const loading        = ref<boolean>(false)
const audioBlob      = ref<Blob|null>(null)
const audioUrl       = ref<string|null>(null)

// emit definition
const emit = defineEmits<{
  (e: 'audio-generated', blob: Blob): void
}>()

const baseUrl = import.meta.env.VITE_ZONOS_API_URL as string

/** ——— Recording logic ——— **/
function startRecording(): void {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then((stream: MediaStream) => {
      const mr = new MediaRecorder(stream)
      recorder.value = mr

      mr.ondataavailable = (e: BlobEvent) => {
        chunks.value.push(e.data)
      }

      mr.onstop = () => {
        const blob = new Blob(chunks.value, { type: 'audio/webm' })
        sampleBlob.value = blob
        chunks.value = []           // reset for next time
        sampleUrl.value = URL.createObjectURL(blob)
      }

      mr.start()
      recording.value = true
    })
    .catch((err: unknown) => {
      console.error('Mic error:', err)
    })
}

function stopRecording(): void {
  if (!recorder.value) return
  recorder.value.stop()
  recording.value = false
}

/** ——— Zonos API call ——— **/
async function generateSpeech(): Promise<void> {
  if (!sampleBlob.value) {
    alert('No recording!')
    return
  }

  loading.value = true

  const form = new FormData()
  form.append('audio_file', sampleBlob.value, 'sample.webm')
  form.append('text', text.value)
  form.append('language', language.value)

  try {
    const resp = await fetch(`${baseUrl}/zonos/`, {
      method: 'POST',
      body: form,
    })
    if (!resp.ok) throw new Error(resp.statusText)

    const blob = await resp.blob()
    audioBlob.value = blob
    audioUrl.value  = URL.createObjectURL(blob)

    // notify parent
    emit('audio-generated', blob)
  } catch (e: any) {
    alert('Error: ' + e.message)
  } finally {
    loading.value = false
  }
}
</script>
