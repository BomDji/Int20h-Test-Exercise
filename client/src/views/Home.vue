<template>
    <div class="home">
        <MainPage/>
        <Search/>
    </div>
</template>

<script>
import MainPage from '@/components/MainPage.vue'
import Search from '@/components/Search.vue'

export default {
    name: 'Home',
    components: {
        MainPage,
        Search
    }
}
</script>