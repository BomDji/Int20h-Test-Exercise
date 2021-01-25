<template>
    <div class="root">
        <v-card
            class="mx-auto text-center mt-10"
            color="grey darken-4"
            dark
            max-width="600"
        >
        <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)">
            <v-sparkline
            :value="value"
            color="rgba(255, 255, 255, .7)"
            height="100"
            padding="24"
            stroke-linecap="round"
            smooth
            >
            <template v-slot:label="item">
                ${{ item.value }}
            </template>
            </v-sparkline>
        </v-sheet>
        </v-card-text>

        <v-card-text>
        <div class="display-1 font-weight-thin">
            Графік найдешевших товарів
        </div>
        </v-card-text>

    <v-divider>

    </v-divider>

    <v-card-actions class="justify-center">
      <v-btn
        block
        text
      >
        Go to Report
      </v-btn>
    </v-card-actions>
  </v-card>
    </div>

</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios)

export default {
    name: 'Chart',
    data: () => ({
      value: [
        423,
        446,
        675,
        510,
        590,
        610,
        760,
      ],
    }),
    mounted(){
        Vue.axios.get('http://127.0.0.1:5000/api/buckwheat_products',)
        .then((resp)=>{
            this.list=resp.data.products;
            console.log(this.list)
        })
    },
    methods: { 
        ReverseList(list) {
                this.list = list.slice().reverse();
            }
        }
}
</script>