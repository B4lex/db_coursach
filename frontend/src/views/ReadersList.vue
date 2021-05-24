<template>
  <div>
    <Readers class="d-flex flex-wrap justify-center" />
    <AddReader class="mx-auto" />
  </div>
</template>

<script>
import AddReader from "../components/AddReader.vue";
import Readers from "../components/Readers.vue";

export default {
  components: {
    Readers,
    AddReader,
  },
};
</script>
