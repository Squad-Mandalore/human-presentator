<template>
  <div>
    <RadarChart :chartConfig="chartConfig" />
  </div>
</template>

<script lang="ts">
import RadarChart from './RadarChart.vue';
import { data, options } from './darkHardSkillChartConfig.ts';

export default {
  components: {
    RadarChart
  },
  data() {
    return {
      chartConfig: { data, options }
    };
  }
}
</script>
