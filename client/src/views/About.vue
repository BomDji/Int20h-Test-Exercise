<template>
    <div class="home">
        <img src="../assets/logo.png" alt="">
        <ProductPage/>
    </div>
</template>

<script>
import ProductPage from '@/components/ProductPage.vue'

export default {
    name: 'About',
    components: {
        ProductPage
    }
}
</script>