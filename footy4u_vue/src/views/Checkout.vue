<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box"> <!-- shadowed contents -->
                <table class="table is-fullwidth"> <!-- table that fills up the page -->
                    <thead>
                        <tr>
                            <th>Game</th>
                            <th>Price</th>
                            <th>Quantity (players)</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items" v-bind:key="item.game.id"> <!-- loops through cart.items -->
                            <td>{{ item.game.name }}</td>
                            <td>£{{ item.game.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>£{{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>£{{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline"> <!-- makes the fields next to each other depending on device -->
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                                <!-- first name field in order to pay -->
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                                <!-- last name field in order to pay -->
                            </div>
                        </div>

                        <div class="field">
                            <label>Email*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email"> <!-- email field in order to pay -->
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone"> <!-- phone field in order to pay -->
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address"> <!-- address field in order to pay -->
                            </div>
                        </div>

                        <div class="field">
                            <label>Post code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="postcode">
                                <!-- post code field in order to pay -->
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place"> <!-- place field in order to pay -->
                            </div>
                        </div>
                    </div>
                </div>
                <div class="notification is-danger mt-4" v-if="errors.length">
                    <!-- displays red errors to users, only generated when errors has length -->
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p> <!-- loops errors -->
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength"> <!-- shows the button to pay ONLY IF THERE IS GAMES IN THE CART -->
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {}, // stripe field
            card: {}, // card field
            first_name: '', // name field
            last_name: '', // last name field
            email: '', // email field
            phone: '', // phone field 
            address: '', // address field
            postcode: '', // postcode field
            place: '', // place field
            errors: [] // errors 
        }
    },
    mounted() {
        document.title = 'Checkout | Footy4U' // shows user which page currently on via the tab on browser

        this.cart = this.$store.state.cart // gets information from the state of the cart

        if (this.cartTotalLength > 0) { // means we have games in the cart
            this.stripe = Stripe('pk_test_51MccryG7xFrGFVYQYfpjSGgiZ3oDehbwZ3MsgWGmF22nhuABes2GE7fCAviOJP11OGA8v4Q8IijP2ZLAaEyw1vNj00NN8FlYVi') // new instance of stripe
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true }) // hides postal code from the form

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.game.price // total calculation of the cart
        },
        submitForm() {
            this.errors = [] // resets errors list

            if (this.first_name === '') {
                this.errors.push('The first name field is missing!') // if first name field has nothing inside it will push this error code to the user
            }
            if (this.last_name === '') {
                this.errors.push('The last name field is missing!') // if last name field has nothing inside it will push this error code to the user
            }
            if (this.email === '') {
                this.errors.push('The email field is missing!') // if email field has nothing inside it will push this error code to the user
            }
            if (this.phone === '') {
                this.errors.push('The phone field is missing!') // if phone field has nothing inside it will push this error code to the user
            }
            if (this.address === '') {
                this.errors.push('The address field is missing!') // if address field has nothing inside it will push this error code to the user
            }
            if (this.postcode === '') {
                this.errors.push('The post code field is missing!') // if post code field has nothing inside it will push this error code to the user
            }
            if (this.place === '') {
                this.errors.push('The place field is missing!') // if place field has nothing inside it will push this error code to the user
            }

            if (!this.errors.length) { // if no errors
                this.$store.commit('setIsLoading', true) // set loading bar to true

                this.stripe.createToken(this.card).then(result => { // based on card information
                    if (result.error) {
                        this.$store.commit('setIsLoading', false) // if there are errors we remove the loading 

                        this.errors.push('Something went wrong with Stripe. Please try again') // error displayed message

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token) // if no errors happened, we proceed to this function
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = [] // new empty list

            for (let i = 0; i < this.cart.items.length; i++) { // loop through the whole cart
                const item = this.cart.items[i]
                const obj = {
                    game: item.game.id,
                    quantity: item.quantity,
                    price: item.game.price * item.quantity
                }

                items.push(obj) // pushes obj to the list of items for better formatting in the backend 
            }

            const data = { // contact information
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'postcode': this.postcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id // retrieved from the backend 
            }

            await axios
                .post('/api/v1/checkout/', data) // post method using contact information
                .then(response => {
                    this.$store.commit('clearCart') // clears cart once user pays
                    this.$router.push('/cart/success') // redirects user to succcess once payment went through
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again') // errors encountered whilst paying pushes this message to users

                    console.log(error)
                })

            this.$store.commit('setIsLoading', false) // remove set is loding
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => { // reduce is a built in JavaScript function, loop through all items in the cart
                return acc += curVal.quantity // acc = accumalator whenever adds more items to the cart it gets passed into the parameter
            }, 0) // default value = 0, 0 + 1...
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.game.price * curVal.quantity // takes the price of the game and multiplies it by the quantity
            }, 0)
        }
    }
}
</script>