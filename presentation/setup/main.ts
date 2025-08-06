import { defineAppSetup } from '@slidev/types'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

export default defineAppSetup(({ app, router }) => {
  // Vue App
  const vuetify = createVuetify({
    components,
    directives,
  })
  app.use(vuetify)
})
