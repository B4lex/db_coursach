<template>
  <v-container>
    <Books class="d-flex justify-center flex-wrap"/>
    <AddBook class="mt-1"/>
  </v-container>
</template>

<script>
import Books from "../components/Books.vue";
import AddBook from "../components/AddBook.vue"

export default {
  data: () => ({
    showAddForm: false
  }),
  components: {
    Books,
    AddBook
  },
};
</script>

<style scoped>

</style>
