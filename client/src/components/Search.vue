<template>
    <div class="root">
        <div class="w-3 h-2 d-flex">
            <v-text-field
            style="background: rgba(255,255,255, 0.8); max-width: 500px; margin: auto;"
            v-model="SearchTitle"
            @click:input="SearchProduct"
            class="pa-3"
            outlined
            label="Я шукаю..."
            append-icon="mdi-magnify"
            hide-details
            clearabl
            >
            </v-text-field>
        </div>

        <div v-if="items!==null" style="max-width: 500px; margin: auto; max-height: 500px;">
            <template>
            <v-container fluid>
                <v-data-iterator
                :items="items"
                :sort-by="sortBy.toLowerCase()"
                :sort-desc="sortDesc"
                hide-default-footer
                disable-pagination
                >
                <template v-slot:header>
                    <v-toolbar
                    dark
                    color="blue darken-3"
                    class="mb-1"
                    >
                    <template v-if="$vuetify.breakpoint.mdAndUp">
                        <v-spacer></v-spacer>
                        <v-select
                        v-model="sortBy"
                        flat
                        solo-inverted
                        hide-details
                        :items="keys"
                        prepend-inner-icon="mdi-magnify"
                        label="Sort by"
                        ></v-select>
                        <v-spacer></v-spacer>
                        <v-btn-toggle
                        v-model="sortDesc"
                        mandatory
                        >
                        </v-btn-toggle>
                    </template>
                    </v-toolbar>
                </template>

                <template v-slot:default="props">
                    <v-row style="max-height: 400px; overflow: scroll;" >
                    <v-col
                        v-for="(item, index) in props.items"
                        :key="index"
                        cols="12"
                        sm="12"
                        md="12"
                        lg="12"
                    >
                        <v-card>
                        <div class="subheading font-weight-bold">
                            {{ item.name }}
                        </div>
                        <v-divider></v-divider>

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
                    </v-col>
                    </v-row>
                </template>

                </v-data-iterator>
            </v-container>
            </template>
        </div>
    </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios)

export default {
  name: 'Search',
  data: () => ({
    SearchTitle: '',
        search: '',
        filter: {},
        sortDesc: false,
        sortBy: 'name',
        keys: [
          'name',
          'price',
        ],
        items: null,
  }),
  computed: {
        // numberOfPages () {
        // return Math.ceil(this.items.length / this.itemsPerPage)
        // },
        filteredKeys () {
            return this.keys.filter(key => key !== 'Name')
        },
    },
    methods:{
        SearchProduct(){
        const url = 'http://127.0.0.1:5000/api/search_products/' + this.SearchTitle;
        Vue.axios.get(url,)
            .then((resp)=>{
                console.log(this.items);
                this.items=resp.data.products;
                console.log(this.items);
            })
        },
    }
}

</script>
