<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
                <h2>Logged in as: <b>{{ this.username }}</b></h2> <!-- displays username at top of the page -->
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My Games</h2>

                <OrderSummary v-for="order in orders" v-bind:key="order.id" v-bind:order="order" />
                <!-- pass in information about the order summary -->
            </div>
            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
                <!-- button to log out of account, red colour to understand what it does -->
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My Account | Footy4U' // shows user which page currently on via the tab on browser

        this.getMyOrders()
        this.created()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token") // removes token from local storage which is needed to logout of an account
            localStorage.removeItem("username") // removes username from local storage which is needed to logout of an account
            localStorage.removeItem("userid") // removes userid from local storage which is needed to logout of an account

            this.$store.commit('removeToken') // updates the state

            this.$router.push('/') // redirect user to home page when user has logged out
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('api/v1/orders/') // get method to orders
                .then(response => {
                    this.orders = response.data // list of orders
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },
        async created() {
            this.username = localStorage.getItem('username')
        }

    },
}
</script>