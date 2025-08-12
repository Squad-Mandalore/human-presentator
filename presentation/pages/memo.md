<div class="h-full flex flex-col">

# Memoavatar Memo
  <div class="flex flex-1 flex-col">
    <div class="flex flex-1 items-start justify-start relative">
      <img src="/memo-overview.jpg" alt="memo architecture picture" class="object-contain" style="width: 65%;"/>
      <div class="absolute" style="top: 0%; left: -1%;">
        <span v-mark.circle="{ at: 2, color: 'red' }" class="text-transparent text-3xl leading-tight">●●●●●●●<br><br>●</span>
      </div>
      <div class="absolute" style="top: 46%; left: 0%;">
        <span v-mark.circle="{ at: 2, color: 'red' }" class="text-transparent text-3xl leading-tight">●●●●●</span>
      </div>
      <div class="absolute" style="top: 47%; left: 52%;">
        <span v-click="5" v-mark.underline="{ at: 5, color: 'red' }" class="underline-close">1.</span>
      </div>
      <div class="absolute" style="top: 52%; left: 52%;">
        <span v-click="6" v-mark.underline="{ at: 6, color: 'red' }" class="underline-close">2.</span>
      </div>
      <div class="absolute" style="top: 57%; left: 52%;">
        <span v-click="7" v-mark.underline="{ at: 7, color: 'red' }" class="underline-close">3.</span>
      </div>
    </div>
  </div>
  <Arrow v-click="'3'" x1="175" y1="110" x2="235" y2="110" color="red" width="1" />
  <Arrow v-click="'4'" x1="235" y1="200" x2="235" y2="230" color="red" width="1" />
  <Arrow v-click="'8'" x1="490" y1="228" x2="550" y2="228" color="red" width="1" />
  <Arrow v-click="'10'" x1="700" y1="100" x2="750" y2="200" color="red" width="5" />
  <Arrow v-click="'11'" x1="800" y1="100" x2="800" y2="200" color="red" width="5" />
  <Arrow v-click="'12'" x1="900" y1="100" x2="850" y2="200" color="red" width="5" />
</div>
<div class="absolute bottom-4 right-4 w-1/3" v-mark.circle="{ at: 9, color: 'red' }">
  <SlidevVideo v-click autoplay controls @timeupdate="onTimeUpdate">
    <source src="/memo-video2.mp4" type="video/mp4" />
    <p>
      Your browser does not support videos. You may download it
      <a href="/memo-video2.mp4">here</a>.
    </p>
  </SlidevVideo>
</div>

<script setup>
import { ref } from 'vue'

const triggered = ref(false)
const arrow1Triggered = ref(false)
const arrow2Triggered = ref(false)
const arrow3Triggered = ref(false)
const number1Triggered = ref(false)
const number2Triggered = ref(false)
const number3Triggered = ref(false)
const videoCircleTriggered = ref(false)
const videoArrow1Triggered = ref(false)
const videoArrow2Triggered = ref(false)
const videoArrow3Triggered = ref(false)

function onTimeUpdate(event) {
  const currentTime = event.target.currentTime
  
  if (currentTime >= 10 && !triggered.value) {
    triggered.value = true
    $slidev.nav.next()
  }
  
  if (currentTime >= 23 && !arrow1Triggered.value) {
    arrow1Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 32 && !arrow2Triggered.value) {
    arrow2Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 50 && !number1Triggered.value) {
    number1Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 55 && !number2Triggered.value) {
    number2Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 60 && !number3Triggered.value) {
    number3Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 66 && !arrow3Triggered.value) {
    arrow3Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 76 && !videoCircleTriggered.value) {
    videoCircleTriggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 77 && !videoArrow1Triggered.value) {
    videoArrow1Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 78 && !videoArrow2Triggered.value) {
    videoArrow2Triggered.value = true
    $slidev.nav.next()
  }

  if (currentTime >= 79 && !videoArrow3Triggered.value) {
    videoArrow3Triggered.value = true
    $slidev.nav.next()
  }
}
</script>

<Footer />

<style>
p {
  margin-top: 0px;
  margin-bottom: 0px;
}

pre code {
  font-size: 0.75em;
}

.underline-close {
  line-height: 0.6 !important;
  display: inline-block;
}

.underline-close svg {
  transform: translateY(-8px) !important;
}
</style>


<!-- 
Introduction of State-of-the-Art (2024) Memo how it works and what differs from
other models. Additionally how we used it in the project and what it can do 
-->

<!-- Check 8 -->
<!-- Dieses Diagramm zeigt, wie MemoAvatar aus Audio realistische sprechende Avatare generiert. Es beginnt mit drei Haupteingaben: einem Referenzbild der Person, um die Identität konsistent zu halten, früheren Videobildern für flüssige Bewegungen und dem Audio, das sie sprechen sollen. -->

<!-- Check 1 -->
<!-- Zunächst komprimiert ein VAE-Encoder das Referenzbild und die früheren Frames in eine kleinere „latente” Form, damit die Verarbeitung schneller erfolgt. -->

<!-- Check 2 -->
<!-- Gleichzeitig wird das Audio durch einen Sprachmerkmalextraktor (Wav2Vec) und einen Emotionsdetektor geleitet, sodass das System sowohl weiß, was gesagt wird, als auch wie es emotional gesagt wird. -->

<!-- Check 4 -->
<!-- Diese Latenten werden in ein Diffusionsmodell eingespeist, stellen Sie sich das wie einen KI-Künstler vor, der mit verrauschten Daten beginnt und diese Schritt für Schritt zu einem klaren Videobild bereinigt. -->

<!-- Check 5 -->
<!-- Dieser Diffusionsprozess wird von drei Modulen gesteuert: einem räumlichen Modul (um das Gesicht der Person anzupassen), einem Audio-Emotionsmodul (um Lippen und Mimik zu synchronisieren) und einem speichergesteuerten Zeitmodul (um die Bilder über die Zeit hinweg konsistent zu halten). -->

<!-- Check 6 -->
<!-- Schließlich wandelt der VAE-Decoder die bereinigten Latenten wieder in ein hochwertiges Videobild um, und der Prozess wiederholt sich für das nächste Bild. -->

<!-- Check 7 -->
<!-- Das Ergebnis ist ein flüssiger, identitätsgetreuer, lippensynchroner und emotional ausdrucksstarker sprechender Avatar. -->


