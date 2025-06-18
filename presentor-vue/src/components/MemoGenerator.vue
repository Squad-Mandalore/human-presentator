<template>
  <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200 space-y-6">
    <div class="flex items-center space-x-3">
      <div class="w-8 h-8 bg-purple-500 text-white rounded-full flex items-center justify-center font-bold">2</div>
      <h2 class="text-2xl font-semibold text-gray-800">Generate Memo Video</h2>
    </div>

    <!-- Method selection -->
    <div class="flex space-x-4 mb-4">
      <label class="flex items-center">
        <input 
          type="radio" 
          v-model="inputMethod" 
          value="camera"
          class="mr-2"
        />
        Use camera
      </label>
      <label class="flex items-center">
        <input 
          type="radio" 
          v-model="inputMethod" 
          value="upload"
          class="mr-2"
        />
        Upload image file
      </label>
    </div>

    <!-- Video preview from webcam -->
    <div v-if="inputMethod === 'camera'" class="space-y-2">
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

    <!-- File upload -->
    <div v-if="inputMethod === 'upload'" class="space-y-2">
      <input
        ref="fileInput"
        type="file"
        accept="image/*"
        @change="handleImageUpload"
        class="block w-full text-sm text-gray-500
               file:mr-4 file:py-2 file:px-4
               file:rounded-full file:border-0
               file:text-sm file:font-semibold
               file:bg-purple-50 file:text-purple-700
               hover:file:bg-purple-100"
      />
    </div>

    <!-- Show captured/uploaded image -->
    <div v-if="photoUrl" class="space-y-2">
      <img :src="photoUrl" class="w-48 h-48 object-cover rounded-full mx-auto" />
      <button
        v-if="inputMethod === 'camera'"
        class="px-4 py-2 bg-gray-300 rounded"
        @click="retake"
      >Retake</button>
      <button
        v-if="inputMethod === 'upload'"
        class="px-4 py-2 bg-gray-300 rounded"
        @click="clearUpload"
      >Clear</button>
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
      <video :src="videoUrl" controls preload="metadata" class="w-full"></video>
      <a
        :href="videoUrl"
        download="memo-video.mp4"
        class="inline-block mt-1 px-4 py-2 bg-green-600 text-white rounded"
      >Download MP4</a>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref, defineProps, watch } from 'vue'
interface Props { audioBlob: Blob }
const props = defineProps<Props>()

const baseUrl = import.meta.env.VITE_MEMO_API_URL

const inputMethod = ref('camera')
const videoEl = ref(null)
const photoBlob = ref(null)
const photoUrl = ref(null)
const photoCaptured = ref(false)
const loading = ref(false)
const videoUrl = ref(null)
const fileInput = ref(null)
const currentStream = ref(null)

// Camera management functions
async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true })
    if (videoEl.value) {
      videoEl.value.srcObject = stream
      currentStream.value = stream
    }
  } catch (err) {
    console.error('Camera access error:', err)
  }
}

function stopCamera() {
  if (currentStream.value) {
    currentStream.value.getTracks().forEach(track => track.stop())
    currentStream.value = null
  }
  if (videoEl.value) {
    videoEl.value.srcObject = null
  }
}

// Watch for input method changes
watch(inputMethod, async (newMethod) => {
  if (newMethod === 'camera') {
    await startCamera()
  } else {
    stopCamera()
  }
})

// Initialize camera on mount if camera method is selected
onMounted(async () => {
  if (inputMethod.value === 'camera') {
    await startCamera()
  }
})

// Cleanup on unmount
onUnmounted(() => {
  stopCamera()
})

// snapshot logic with square cropping from center
function capturePhoto() {
  const video = videoEl.value
  if (!video || !video.videoWidth || !video.videoHeight) return
  
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  
  // Calculate square dimensions (minimum of width/height)
  const squareSize = Math.min(video.videoWidth, video.videoHeight)
  canvas.width = squareSize
  canvas.height = squareSize
  
  // Calculate center crop coordinates
  const cropX = (video.videoWidth - squareSize) / 2
  const cropY = (video.videoHeight - squareSize) / 2
  
  // Draw the square crop from center of video
  ctx.drawImage(
    video,
    cropX, cropY, squareSize, squareSize, // source rectangle
    0, 0, squareSize, squareSize // destination rectangle
  )
  
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

// file upload logic
function handleImageUpload(event) {
  const target = event.target
  const file = target.files?.[0]
  if (!file) return

  photoBlob.value = file
  photoUrl.value = URL.createObjectURL(file)
  photoCaptured.value = true
}

function clearUpload() {
  photoBlob.value = null
  photoUrl.value = null
  photoCaptured.value = false
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

// send to Memo API
async function generateVideo() {
  loading.value = true
  
  // Clean up previous video URL to ensure fresh load
  if (videoUrl.value) {
    URL.revokeObjectURL(videoUrl.value)
    videoUrl.value = null
  }
  
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
