<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4"> <!-- middle of the screen  -->
                <h1 class="title">Sign up</h1>

                <form @submit.prevent="submitForm"> <!-- form, prevent to submit to server -->
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                            <!-- creating username, input has to be text attribute -->
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                            <!-- creating password, input has to be text attribute -->
                        </div>
                    </div>
                    <div class="field">
                        <label>Re-enter Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                            <!-- checking password matches, input has to be text attribute -->
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <!-- displays red errors to users, only generated when errors has length -->
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p> <!-- loops errors -->
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Sign Up</button>
                            <!-- button to signup once user has filled in all fields -->
                        </div>
                    </div>
                    <hr>
                    Have an account already? <router-link to="/log-in">Click here</router-link> to log in!
                    <!-- if user has account, user can quickly navigate to the log in page -->
                </form>
            </div>
        </div>
    </div>
</template>

<script>



import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name: 'SignUp',
    data() {
        return {
            username: '', // creating username
            password: '', // creating password
            password2: '', // checking password matches
            email: '', // create email
            errors: [] // checking errors when signing up
        }
    },
    mounted() {
        document.title = 'Sign Up | Footy4U' // shows user which page currently on via the tab on browser
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing') // if username field has nothing inside it will push this error code to the user
            }

            if (this.password === '') {
                this.errors.push('The password is too short') // if password is too short it will push this error code to the user
            }

            if (this.password2 === '') {
                this.errors.push('The passwords do not match') // if password do not match it will push this error code to the user 
            }

            if (!this.errors.length) { // IF THERE IS NO ERRORS 
                const formData = {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }

                axios
                    .post("/api/v1/users/", formData) // posts to this route
                    .then(response => { // expect response
                        toast({
                            message: 'Account has been created, please log in!', // success message displayed
                            type: 'is-success', // green colour
                            dismissible: true, // user can remove message
                            pauseOnHover: true, // message will be paused to user if hovered
                            duration: 2000, // // 2000ms = 2 secs time of notification being shown to user
                            position: 'bottom-right' // notification placed at bottom right of the screen
                        })
                        this.$router.push('/log-in') // once user signed up, automatically redirects you to log in screen
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) { // loop through the errors recieved from the server 
                                this.errors.push(`${property}: ${error.response.data[property]}`) // push errors to the user from the server 
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}

</script>