import Vue from 'vue';
import VueRouter from 'vue-router';
// import About from '../views/About.vue';
import Home from '../views/Home.vue';
import Buckwheat from '../views/Buckwheat.vue';
import Product from '../views/Product.vue';
import Chart from '../views/Chart.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/buckwheat',
        name: 'Buckwheat',
        component: Buckwheat
    },
    {
        path: '/product',
        name: 'Product',
        component: Product
    },
    {
        path: '/chart',
        name: 'Chart',
        component: Chart
    }
]

const router = new VueRouter({
    routes
})

export default router