<template>
  <v-app id="inspire">

    <v-navigation-drawer
      v-model="drawer"
      color="grey darken-4"
      app
      dark
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Товари
          </v-list-item-title>
          <v-list-item-subtitle>
            Виберіть потрібний товар
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar color="grey darken-4" dark app style="width: 100vw;">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-system-bar
        window
        color="grey darken-4"
      >
        <v-icon>mdi-cash-multiple</v-icon>
        <span>Найдешевша гречка: {{minProductObject.price}} {{minProductObject.currency}} в <a :href="minProductObject.link">{{minProductObject.shop_name}}</a></span>
        <v-spacer></v-spacer>
      </v-system-bar>

    </v-app-bar>

    <v-img

      max-height="800"
      gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
      src="./assets/grechka.png"
    >
      <v-main>
        <router-view></router-view>
      </v-main>
    </v-img>
    <Footer/>
  </v-app>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios)

import Footer from './components/Footer';

export default {
  name: 'App',

  components: {
    Footer
  },

  data: () => ({
    SearchTitle: '',
    drawer: null,
    items: [
          { title: 'Головна сторінка', icon: 'mdi-home-circle', to: '/' },
          { title: 'Графік', icon: 'mdi-chart-areaspline', to: '/chart' },
          { title: 'Гречка',  icon: 'mdi-shopping-outline', to: '/buckwheat' },
        ],
    info: null,
    minProductObject: {}
  }),
  mounted(){
        Vue.axios.get('http://64.225.99.61:5000/api/minimum_buckwheat_price',)
        .then((resp)=>{
            this.minProductObject=resp.data;
        })
  },

};

</script>
