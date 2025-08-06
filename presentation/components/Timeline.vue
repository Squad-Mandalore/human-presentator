<template>
  <v-timeline style="grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr)" direction="horizontal">
    <v-timeline-item
      class="mx-auto"
      dot-color="#187B3C"
    >
      <template v-slot:opposite>
        <div class="text-h6">Praktikum 2018</div>
        <p>
          Erstes mal eine Vision von Teamwork im Arbeitsumfeld. Website Programmierung.
        </p>
      </template>
      <div>
        <strong>Performics Germany GmbH</strong>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#96131B"
    >
      <template v-slot:opposite>
        <strong>OSZ IMT</strong>
      </template>
      <div>
        <div class="text-h6">Abitur mit IT Leistungskurs 2019-2022</div>
        <p>
          Erste Erfahrungen mit Java. Leidenschaft entfacht.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#E20074"
    >
      <template v-slot:opposite>
        <div class="text-h6">Onboarding 2022-2024</div>
        <p>
          Einführung in den Workflow eines Fullstack Engineers.
        </p>
      </template>
      <div>
        <strong>DTIT Gigabit + Studium</strong>
      </div>
    </v-timeline-item>

    <v-timeline-item
      class="mx-auto"
      dot-color="#E20074"
    >
      <template v-slot:opposite>
        <strong>DTIT B2B Solutions API + Studium</strong>
      </template>
      <div>
        <div class="text-h6">Praktische Erfahrungen 2024-2025</div>
        <p>
          Neue Einblicke und tiefere Erfahrung in DevOps Workflows.
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
</style>
