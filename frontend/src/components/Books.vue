<template>
  <div>
    <Loader v-if="loading"/>
    <BookCard v-else
    v-for="book in books" 
    :key="book.id" 
    :bookData="book"
    style="margin: 10px"
    />
  </div>
</template>

<script>
import { get_all_books } from "../services/books";
import BookCard from './BookCard.vue'
import Loader from './Loader.vue'

export default {
  data: () => ({
    books: [],
    loading: true
  }),
  async mounted() {
    this.books = await get_all_books().then(
        (data) => {
            this.loading = false
            return data;
        });
  },
  components: {
      BookCard,
      Loader
  }
};
</script>