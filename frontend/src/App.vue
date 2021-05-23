<template>
  <div id="app">
    <v-app>
      <LibraryHeader />
      <v-main>
        <router-view />
      </v-main>
    </v-app>
  </div>
</template>

<script>
import LibraryHeader from "./components/LibraryHeader.vue";

export default {
  components: {
    LibraryHeader,
  },
};
</script>

<style>
#app {
  font-family: sans-serif;
}
</style>
