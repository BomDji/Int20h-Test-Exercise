<template>
    <div class="root">
        <div class="mx-auto mt-10 rounded-lg" style="max-width: 400px; height: 400px; overflow: scroll; box-shadow: 0 0 10px rgba(0,0,0,0.5);">
            <v-card v-for="(item, index) in list" v-bind:key="index"
                class="mx-auto"
                max-width="400"
                tile
            >
                <v-list-item three-line>
                    <v-list-item-icon>
                        <img size="24px" style="width:50px" v-bind:src="item.img_link">
                    </v-list-item-icon>
                <v-list-item-content>
                <v-list-item-title style="bold">
                    {{item.name}}
                </v-list-item-title>
                <v-list-item-subtitle>
                    {{item.description}}
                </v-list-item-subtitle>
                <div class="d-inline">
                    <span class="float-left">Ціна: {{item.price}}  {{item.currency}}</span>
                    <span class="float-right">
                    <a :href="item.link">
                        Перейти до {{item.shop_name}}
                    </a>
                    </span>
                </div>
                </v-list-item-content>
                </v-list-item>
            </v-card>
        </div>
        <div class="mx-auto mt-10 rounded-lg" style="text-aling: center !important;">
            <button class="px-5 py-2 mx-auto d-flex white rounded-lg" v-on:click="ReverseList(list)"><v-icon class="px-2">mdi-reload</v-icon>
            Змінити сортування</button>
        </div>
    </div>

</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios)

export default {
    name: 'Buckwheat',
    data(){
        return {list: undefined}
    },
    mounted(){
        Vue.axios.get('http://64.225.99.61:5000/api/buckwheat_products',)
        .then((resp)=>{
            this.list=resp.data.products;
        })
    },
    methods: {
        ReverseList(list) {
                this.list = list.slice().reverse();
            }
        }
}
</script>
