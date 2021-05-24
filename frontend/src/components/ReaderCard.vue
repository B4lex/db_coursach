<template>
  <v-card class="mx-auto" max-width="344" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">Читатель</div>
        <v-list-item-title class="headline mb-1">
          {{ reader.first_name }} {{ reader.last_name }}
        </v-list-item-title>
        <v-list-item-subtitle>Возраст: {{ reader.age }}</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar tile size="80" id="avatar"></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <div class="text-center mr-3">
        <v-btn rounded color="primary" dark @click="giveBook"> Выдать книгу </v-btn>
      </div>
      <v-btn outlined rounded text>Книги</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>



export default {
  props: ["reader"],
  methods: {
    async giveBook() {
        let reader_id = this.reader.id
        
        console.log(this.reader.id)
    },
    async listBooks() {

    },
  },
};
</script>

<style scoped>
#avatar {
  background-image: url("../assets/logo.png");
  background-size: cover;
}
</style>