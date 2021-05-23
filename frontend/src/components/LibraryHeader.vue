<template>
  <div>
    <v-app-bar>
      <router-link to="/books">
        <v-btn depressed>
          <v-icon> mdi-bookshelf </v-icon>
          Книги
        </v-btn>
      </router-link>
      <router-link to="/authors">
        <v-btn depressed @click="$emit('authors-clicked')">
          <v-icon> mdi-book-account </v-icon>
          Авторы
        </v-btn>
      </router-link>
      <router-link to="/readers">
        <v-btn depressed>
          <v-icon> mdi-account </v-icon>
          Читатели
        </v-btn>
      </router-link>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "LibraryHeader",
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}
</style>