import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios' // telling Vue.js to use axios

axios.defaults.baseURL = "http://127.0.0.1:8000" // axios having access to backend url to make api calls between frontend and backend

createApp(App).use(store).use(router, axios).mount('#app')
