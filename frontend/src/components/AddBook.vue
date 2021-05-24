<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          class="add-button"
          fab
          dark
          color="#00CF91"
          v-bind="attrs"
          v-on="on"
        >
          <v-icon dark> mdi-plus </v-icon>
        </v-btn>
      </template>
      <v-card class="pa-5">
        <v-card-title>
          <span class="headline">Добавить книгу</span>
        </v-card-title>
        <form @submit.prevent="submit">
          <v-text-field
            v-model="form.title"
            :counter="64"
            label="Название"
            required
          ></v-text-field>
          <v-textarea
            v-model="form.description"
            :counter="512"
            label="Краткое описание"
            required
          ></v-textarea>
          <v-autocomplete 
          :items="authors_data" 
          :item-text="getAuthorFullName" 
          item-value="id"
          v-model="form.author_id"
          label="Автор"></v-autocomplete>
          <v-text-field
            v-model="form.pages_count"
            :counter="5"
            label="Количество страниц"
            required
          ></v-text-field>
          <v-text-field
            v-model="form.release_date"
            :counter="4"
            label="Год издания:"
            required
          ></v-text-field >
          <v-btn class="mr-4" type="submit" color="green"> Сохранить </v-btn>
          <v-btn @click="dialog = false" color="red"> Закрыть </v-btn>
        </form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { get_all_authors } from '../services/authors'
import { create_book } from '../services/books'


export default {
  data: () => ({
    form: {
      title: null,
      description: null,
      author_id: null,
      genre_id: null,
      stylistics_id: null,
      pages_count: null,
      release_date: null,
      age_restrictions: null
    },
    dialog: false,
    authors_data: []
  }),
  async mounted() {
    this.authors_data = await get_all_authors().then(
      data => {
        console.log(data)
        return data
      }
    )
  },
  methods: {
    getAuthorFullName: item => `${item.first_name} ${item.last_name}`,
    async submit() {
      this.form.release_date = '01-01-' + this.form.release_date
      await create_book(this.form)
      this.dialog = false
    }
  } 
};
</script>
