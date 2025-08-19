<template>
  <div style="height: 22rem;">
    <Bar :data="chartConfig.data" :options="chartConfig.options" />
  </div>
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Bar } from 'vue-chartjs'
import { data, options } from './VRAMChartConfig.ts'

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'VRAMChart',
  components: {
    Bar
  },
  data() {
    return {
      chartConfig: { data, options }
    }
  }
}
</script>
