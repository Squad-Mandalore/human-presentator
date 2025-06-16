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
  <div class="max-w-2xl mx-auto p-6 space-y-10">
    <h1 class="text-3xl font-bold text-center">Zonos + Memo Client</h1>

    <ZonosGenerator @audio-generated="onAudioGenerated" />

    <MemoVideoGenerator
      v-if="generatedAudioBlob"
      :audioBlob="generatedAudioBlob"
    />
  </div>
</template>
