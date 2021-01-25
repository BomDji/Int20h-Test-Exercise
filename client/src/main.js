import Vue from 'vue'
import App from './App.vue'
import Router from './router'
import vuetify from './plugins/vuetify';
import axios from 'axios';

Vue.config.productionTip = false
axios.defaults.headers.get['header-name'] = 'value'

new Vue({
  router: Router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
