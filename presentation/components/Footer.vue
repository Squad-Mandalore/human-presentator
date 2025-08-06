<template>
  <div class="footer">
    <div class="footer-content">
      <p style="margin-top: 0" v-html="formattedFooterMessage"></p>
    </div>
    <div class="page-number">
        <SlideCurrentNo />
    </div>
  </div>
</template>

<style>
.footer {
  margin-top: 1em;
  margin-bottom: 1em;
  text-align: center;
  font-size: 16px;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
}

.footer-content {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-bottom: 0;
}

.page-number {
  margin-top: 0;
}

</style>

<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $slidev, $page } = useSlideContext();

const currentPage = $page;

const footerMessage = computed(() => {
  return $slidev.nav.tocTree;
});

// Helper function to recursively collect titles

function collectTitles(node, list = [], maxCount = 4) {

  if (list.length < maxCount && node.no >= $page.value) {  // Use the currentPage prop here
    list.push(node.title);
  }
  if (list.length < maxCount) {
    node.children.forEach(child => collectTitles(child, list, maxCount));
  }
  return list;
}

// Computed property to create the formatted string from titles
const formattedFooterMessage = computed(() => {
  let titles = [];

  footerMessage.value.forEach(node => {
    if (titles.length < 4) {  // Use the currentPage prop here
      collectTitles(node, titles);
    }
  });

  // Apply bold to the first title and join the rest with ' -> '
  if (titles.length > 0) {
    titles[0] = `<strong>${titles[0]}</strong>`; // Make the first title bold using <strong> tag
  }
  return titles.join(' ￫ '); // Joins all titles with ' -> '
});

</script>

