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
                    :series="series" 
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
import VueApexCharts from 'vue-apexcharts'

Vue.use(VueAxios, axios, VueApexCharts)


Vue.component('apexchart', VueApexCharts)

export default {
    name: 'Chart',
    data: () => ({
      options: {
        chart: {
            type: "line",
            stacked: false
        },
        tooltip: {theme: "dark"},
        stroke:{
            width: 2
        },
        
        xaxis: {
            categories: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
        },
        
        legend: {
            horizontalAlign: "left",
            offsetX: 40
        }
    },
    series: [
        {
        name: "Series A",
        data: [1.4, 2, 2.5, 1.5, 2.5, 2.8, 3.8, 4.6]
        },
        {
        name: "Series B",
        data: [20, 29, 37, 36, 44, 45, 50, 58]
        }
    ],
        
    }),
    mounted(){
        Vue.axios.get('http://127.0.0.1:5000/api/prices_history',)
        .then((resp)=>{
            this.pricesHistory = resp.data.products;
            this.xaxisData = [];
            for(var historyPoint in this.pricesHistory[0].price_history){
                this.xaxisData.push(historyPoint[0][0])
            }
            console.log(this.pricesHistory)
            console.log(this.xaxisData)
        })
    },
    methods: { 
        ReverseList(list) {
                this.list = list.slice().reverse();
            }
        }
}
</script>