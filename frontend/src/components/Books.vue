<template>
  <div>
    <Loader v-if="loading" />
    <BookCard
      v-else
      v-for="book in books"
      :key="book.id"
      :bookData="book"
      style="margin: 10px"
    />
  </div>
</template>

<script>
import { get_all_books } from "../services/books";
import { get_author_by_id } from "../services/authors";
import BookCard from "./BookCard.vue";
import Loader from "./Loader.vue";

export default {
  data: () => ({
    books: [],
    loading: true,
  }),
  async mounted() {
    this.books = await get_all_books().then(async (books_data) => {
      for (let book of books_data) {
        let author = await get_author_by_id(book.author_id)
        book.author = author
        console.log(book)
      }
      this.loading = false;
      return books_data;
    });
  },
  components: {
    BookCard,
    Loader,
  },
};
</script>