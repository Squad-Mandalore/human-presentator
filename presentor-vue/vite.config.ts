import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import autoprefixer from 'autoprefixer'
import postcssTailwind from '@tailwindcss/postcss'

export default defineConfig({
  plugins: [vue()],
  css: {
    postcss: {
      plugins: [
        postcssTailwind(),
        autoprefixer(),
      ]
    }
  },
})
