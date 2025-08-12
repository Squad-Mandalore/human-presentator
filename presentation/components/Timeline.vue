<template>
  <v-timeline style="grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)" direction="horizontal">
    <v-timeline-item
      class="mx-auto"
      dot-color="#FFD700"
    >
      <template v-slot:opposite>
        <div class="text-h6">Ideation</div>
        <p>
          Initial concept development and brainstorming phase.
        </p>
      </template>
      <div>
        <strong>Planning & Design</strong>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#ED8B00"
    >
      <template v-slot:opposite>
        <strong>Single Codebase</strong>
      </template>
      <div>
        <div class="text-h6">Monolithic implementation</div>
        <p>
          All-in-one application structure with tightly coupled components.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#3776AB"
    >
      <template v-slot:opposite>
        <div class="text-h6">API based implementation</div>
        <p>
          Decoupled architecture with REST APIs for data exchange.
        </p>
      </template>
      <div>
        <strong>Backend Services</strong>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#42B883"
    >
      <template v-slot:opposite>
        <strong>User Interface</strong>
      </template>
      <div>
        <div class="text-h6">Frontend implementation</div>
        <p>
          Modern reactive frontend consuming API services.
        </p>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

<style>

html:not(.dark) .v-timeline-divider__before, html:not(.dark) .v-timeline-divider__after {
  background: black;
}

html.dark .v-timeline-divider__before, html.dark .v-timeline-divider__after {
  background: white;
}

html:not(.dark) .v-timeline .v-timeline-divider__dot {
  background: #333333 !important;
}

.v-timeline-item .v-timeline-divider__dot {
  background: #333333 !important;
}

</style>
