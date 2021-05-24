<template>
  <div>
    <Authors />
    <AddAuthor />
  </div>
</template>

<script>
import Authors from '../components/Authors.vue'
import AddAuthor from '../components/AddAuthor.vue'

export default {
  components: {
    Authors,
    AddAuthor
  }
}
</script>
