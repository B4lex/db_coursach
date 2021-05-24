<template>
  <v-container>
    <v-card v-for="author in authors" :key="author.id" max-width="300px">
      <v-card-title>
        {{ author.first_name }}
        {{ author.last_name }}
        <v-card-subtitle v-if="author.birth_date">
          Год рождения: {{ new Date(author.birth_date).getFullYear() }}
        </v-card-subtitle>
      </v-card-title>
    </v-card>
  </v-container>
</template>

<script>
import { get_all_authors } from "../services/authors";

export default {
  data: () => ({
    authors: [],
  }),
  async mounted() {
    this.authors = await get_all_authors();
  },
};
</script>