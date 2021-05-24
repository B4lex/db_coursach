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
          <span class="headline">Добавить автора</span>
        </v-card-title>
        <form @submit.prevent="submit">
          <v-text-field
            v-model="form.first_name"
            :counter="32"
            label="Имя"
            required
          ></v-text-field>
          <v-text-field
            v-model="form.last_name"
            :counter="32"
            label="Фамилия"
            required
          ></v-text-field>
          <v-text-field
            v-model="form.birth_date"
            :counter="4"
            label="Год рождения"
            required
          ></v-text-field>
          <v-btn class="mr-4" type="submit" color="green"> Сохранить </v-btn>
          <v-btn @click="dialog = false" color="red"> Закрыть </v-btn>
        </form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { create_author } from '../services/authors'

export default {
  data: () => ({
    form: {
        first_name: null,
        last_name: null,
        birth_date: null,
        country_id: null
    },
    dialog: false,
  }),
  methods: {
      async submit() {
          this.form.birth_date = '01-01-' + this.form.birth_date
          await create_author(this.form)
          this.dialog = false
      }
  }
};
</script>
