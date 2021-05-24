<template>
    <div class="pa-5">
        <ReaderCard v-for="reader in readers" :key="reader.id" :reader="reader"/>
    </div>
</template>

<script>
import ReaderCard from './ReaderCard.vue'
import { get_all_readers } from '../services/readers.js'


export default {
    data: () => ({
        readers: []
    }),
    components: {
        ReaderCard,
    },
    async mounted() {
        this.readers = await get_all_readers()
    }
}
</script>