<template>
  <div class="p-6 border rounded-lg shadow-lg space-y-4">
    <h2 class="text-2xl font-semibold">2. Generate Memo Video</h2>

    <!-- Video preview from webcam -->
    <div class="space-y-2">
      <video
        ref="videoEl"
        autoplay
        muted
        playsinline
        class="w-full h-64 bg-black rounded"
      ></video>
      <button
        class="px-4 py-2 bg-purple-600 text-white rounded"
        @click="capturePhoto"
        :disabled="photoCaptured"
      >Capture Face Snapshot</button>
    </div>

    <!-- Show captured snapshot & retake -->
    <div v-if="photoUrl" class="space-y-2">
      <img :src="photoUrl" class="w-48 h-48 object-cover rounded-full mx-auto" />
      <button
        class="px-4 py-2 bg-gray-300 rounded"
        @click="retake"
      >Retake</button>
    </div>

    <button
      class="mt-2 w-full py-2 bg-indigo-600 text-white rounded"
      @click="generateVideo"
      :disabled="!props.audioBlob || !photoBlob || loading"
    >
      {{ loading ? 'Rendering…' : 'Generate Video' }}
    </button>

    <!-- Playback & download of result -->
    <div v-if="videoUrl" class="space-y-2">
      <video :src="videoUrl" controls class="w-full"></video>
      <a
        :href="videoUrl"
        download="memo-video.mp4"
        class="inline-block mt-1 px-4 py-2 bg-green-600 text-white rounded"
      >Download MP4</a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, defineProps } from 'vue'
interface Props { audioBlob: Blob }
const props = defineProps<Props>()

const baseUrl = import.meta.env.VITE_MEMO_API_URL

const videoEl = ref(null)
const photoBlob = ref(null)
const photoUrl = ref(null)
const photoCaptured = ref(false)
const loading = ref(false)
const videoUrl = ref(null)

// start webcam
onMounted(async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true })
  videoEl.value.srcObject = stream
})

// snapshot logic
function capturePhoto() {
  const video = videoEl.value
  const canvas = document.createElement('canvas')
  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  canvas.getContext('2d').drawImage(video, 0, 0)
  canvas.toBlob(blob => {
    photoBlob.value = blob
    photoUrl.value = URL.createObjectURL(blob)
    photoCaptured.value = true
  }, 'image/png')
}

function retake() {
  photoCaptured.value = false
  photoBlob.value = null
  photoUrl.value = null
}

// send to Memo API
async function generateVideo() {
  loading.value = true
  const form = new FormData()
  form.append('audio_file', props.audioBlob, 'speech.wav')
  form.append('picture', photoBlob.value, 'face.png')

  const resp = await fetch(`${baseUrl}/memo/`, {
    method: 'POST',
    body: form
  })
  if (!resp.ok) {
    alert('Error: ' + resp.statusText)
    loading.value = false
    return
  }

  const blob = await resp.blob()
  videoUrl.value = URL.createObjectURL(blob)
  loading.value = false
}
</script>
