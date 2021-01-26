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
            <template>
                <div>
                    <apexchart width="500" 
                    :options="options" 
                    :series="pricesHistorySeries" 
                    :xaxis="pricesHistoryXaxis"
                    ></apexchart>
                </div>
            </template>
        </v-sheet>
        </v-card-text>

        <v-card-text>
        <div class="display-1 font-weight-thin">
            Графік найдешевших гречок
        </div>
        </v-card-text>

    <v-divider>

    </v-divider>

    <v-card-actions class="justify-center">
      <v-btn
        block
        text
        href="/"
      >
        Головна сторінка
      </v-btn>
    </v-card-actions>
  </v-card>
    </div>

</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueApexCharts from 'vue-apexcharts'

Vue.use(VueAxios, axios, VueApexCharts)


Vue.component('apexchart', VueApexCharts)

export default {
    name: 'Chart',
    data(){ return{
        
        options: {
            chart: {
                type: "line",
                stacked: false
            },
            tooltip: {theme: "dark"},
            stroke:{
                width: 2
            },
            
            // xaxis: {
            //     categories: pricesHistoryXaxis
            // },
            
            legend: {
                horizontalAlign: "left",
                offsetX: 40
            }
        },
        pricesHistorySeries: [],
        pricesHistoryXaxis: {}
    }
    },

    created () {
        this.initialize()
    },  

    methods: {
        initialize () {
        Vue.axios.get('http://127.0.0.1:5000/api/prices_history',)
        .then((resp)=>{
            this.pricesHistorySeries = resp.data.series;
            this.pricesHistoryXaxis = {'categories':resp.data.xaxis};
        })
    }
    }
}
</script>