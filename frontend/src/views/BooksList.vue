<template>
  <v-container>
    <Books class="d-flex justify-center flex-wrap"/>
    <AddBookForm class="mt-1"/>
  </v-container>
</template>

<script>
import Books from "../components/Books.vue";
import AddBookForm from "../components/AddBookForm.vue"

export default {
  data: () => ({
    showAddForm: false
  }),
  components: {
    Books,
    AddBookForm
  },
};
</script>

<style scoped>

</style>
