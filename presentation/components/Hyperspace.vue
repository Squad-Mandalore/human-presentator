<template>
  <div v-click style="display: none"></div>
  <div v-if="jump" class="hyperspace" ref="wrapper">
    <div class="stars" ref="starsContainer">
      <div
        v-for="(s,i) in stars"
        :key="i"
        class="star"
        :style="starStyle(s)"
      />
    </div>
    <div class="flash" ref="flashContainer" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, nextTick } from 'vue'
import { gsap } from 'gsap'
import { useNav, useSlideContext } from '@slidev/client'

interface Star {
  r: number      // radial
  z: number      // initial depth
  theta: number  // angle (degrees)
}

const jump = ref(false)
const stars = ref<Star[]>([])
const speed = ref(0.5)
const burst = ref(0.0005)
const starsContainer = ref<HTMLElement|null>(null)
const flashContainer = ref<HTMLElement|null>(null)

const nav = useNav()
const {$slidev, $page} = useSlideContext()


onMounted(() => {
  // number of stars
  const N = 2000
  const W = window.innerWidth
  const H = window.innerHeight
  const maxR = Math.hypot(W/2, H/2)
  const D = 2000
  // no‐star radius
  const safeR = 50

  for (let i = 0; i < N; i++) {
    const r = safeR + Math.random()*(maxR - safeR)
    const rad = Math.random()*Math.PI*2
    const theta = rad * (180/Math.PI) + 90
    const z = -Math.random()*D
    stars.value.push({ r, z, theta })
  }
})

function starStyle(s: Star) {
  return {
    transform: [
      // start at screen‐center, push back in Z
      `translateZ(${s.z}px)`,
      // spin the star so it’s pointing directly at the camera
      `rotateZ(${s.theta}deg)`,
      // slide it out along its own Y axis by its radius
      `translateY(${s.r}px)`
    ].join(' '),
    // pivot at the “top” of the div
    transformOrigin: '50% 0%'
  }
}

function triggerJump() {
  jump.value = true
}

watch(jump, async (isOn) => {
  if (!isOn) return
  await nextTick()
  const starsEls = starsContainer.value!.children
  const flashEl  = flashContainer.value!
  const tl = gsap.timeline({ onComplete: () => {
    }
  })

  tl.timeScale(speed.value)

  // fly forward in Z *and* stretch each line
  tl.to(starsEls, {
    translateZ:  800,
    scaleY:      8,
    opacity:     0,
    duration:    2,
    stagger:     burst.value,
    ease:        'power2.out'
  }, 0)

  // quick white flash
  tl.fromTo(flashEl,
    { opacity: 0 },
    { opacity: 1, duration: 0.1, ease: 'none' },
    0.9
  )
  tl.to(flashEl,
    {
      opacity: 0,
      duration: 0.3,
      onStart: () => {
        window.open('http://localhost:8000', '_blank')
        nav.nextSlide()
      },
      onComplete: () => {
        jump.value = false
      }
    },
    '>'
  )
})

watch(
  () => nav.clicks.value,
  (clickCount) => {
    if (clickCount === $slidev.nav.clicksTotal && $slidev.nav.currentSlideNo === $page.value) {
      if ($slidev.nav.clicksDirection === -1) {
        $slidev.nav.prev()
        return
      }
      triggerJump()
    }
  },
)
</script>

<style>
.hyperspace {
  position: fixed;
  inset: 0;
  perspective: 800px;
  overflow: hidden;
}
.stars {
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
}
.star {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1px;
  height: 20px;
  background: black;
  will-change: transform, opacity;
}
.flash {
  position: absolute;
  inset: 0;
  background: white;
  opacity: 0;
  pointer-events: none;
}
</style>
