<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4"> <!-- middle of the screen  -->
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm"> <!-- form, prevent to submit to server -->
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username"> <!-- username field to login -->
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password"> <!-- password field to login -->
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <!-- displays red errors to users, only generated when errors has length -->
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p> <!-- loops errors -->
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log in</button> <!-- button to login -->
                        </div>
                    </div>
                    <hr>
                    Don't have an account? <router-link to="/sign-up">Click here</router-link> to sign up!
                    <!-- link to user if user does not have an account and has landed on the login page -->
                </form>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | Footy4U' // shows user which page currently on via the tab on browser
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = "" // reset authorization from earlier session

            localStorage.removeItem("token") // remove token from earlier session

            const formData = { // creating form of data for users to perfrom the login functionality
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData) // post method for the token login
                .then(response => {
                    const token = response.data.auth_token
                    const username = this.username // retrieve current username logged in

                    this.$store.commit('setToken', token) // calls store to set the token, found from server information

                    axios.defaults.headers.common['Authorization'] = "Token " + token // everytime we call the server, we have already set the token

                    localStorage.setItem("token", token) // store token in local storage, when refreshing it will still work
                    localStorage.setItem("username", username) // store username in local storage 

                    const toPath = this.$route.query.to || '/cart' // we want to go to the path we are coming from, so a non-registered user proceeding to the checkout must login first!

                    this.$router.push(toPath) // when logged in, you will be redirected when you signed in 
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) { // loop through the errors recieved from the server 
                            this.errors.push(`${property}: ${error.response.data[property]}`) // push errors to the user from the server
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>