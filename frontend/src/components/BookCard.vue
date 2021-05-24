<template>
    <v-card
      max-width="344"
    >
      <v-img
        src="../assets/books.jpg"
        height="200px"
      ></v-img>

      <v-card-title> {{ bookData.title }} </v-card-title>

      <v-card-subtitle>
        {{ new Date(bookData.release_date).getFullYear() }}
      </v-card-subtitle>
      <v-card-text>
        Автор:
        {{ bookData.author.first_name }} {{ bookData.author.last_name }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="orange lighten-2" text @click="show = !show">
            Краткое описание
            <v-icon>{{ show ? "mdi-chevron-up" : "mdi-chevron-down" }}</v-icon>
        </v-btn>
      </v-card-actions>

      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>

          <v-card-text>
            {{ bookData.description }}
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
</template>


<script>
export default {
    data: () => ({
        show: false,
    }),
    props: [
        'bookData'
    ]
}
</script>