<script setup lang="ts">
import { ref } from 'vue'
import ZonosGenerator from './components/ZonosGenerator.vue'
import MemoVideoGenerator from './components/MemoGenerator.vue'

const generatedAudioBlob = ref<Blob|null>(null)

// when Zonos returns audio, we capture it here:
function onAudioGenerated(blob: Blob) {
  generatedAudioBlob.value = blob
}
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-purple-100">
    <div class="max-w-4xl mx-auto p-8 space-y-8">
      <header class="text-center space-y-4">
        <h1 class="text-4xl font-bold text-gray-800">
          🎭 Human Presenter Generator
        </h1>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto">
          Create realistic human presenters by combining voice samples and face images. 
          Use your microphone and camera or upload existing files.
        </p>
      </header>

      <div class="grid gap-8 lg:grid-cols-1">
        <ZonosGenerator @audio-generated="onAudioGenerated" />

        <div v-if="generatedAudioBlob" class="transition-all duration-300 ease-in-out">
          <MemoVideoGenerator :audioBlob="generatedAudioBlob" />
        </div>
        
        <div v-else class="p-8 text-center bg-white/50 rounded-lg border-2 border-dashed border-gray-300">
          <div class="text-gray-500">
            <p class="text-lg font-medium">Step 2 will appear here</p>
            <p class="text-sm">Complete step 1 to generate speech first</p>
          </div>
        </div>
      </div>

      <footer class="text-center text-sm text-gray-500 pt-8 border-t">
        <p>Powered by Zonos (voice synthesis) + Memo (face animation)</p>
      </footer>
    </div>
  </div>
</template>
