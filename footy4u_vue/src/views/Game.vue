<template>
    <div class="page-game"> <!-- to make sure which page  -->
        <div class="columns is-multiline">
            <div class="column is-9"> <!-- left of the screen to show images and title -->
                <figure class="image mb-6"> <!-- more space below -->
                    <img v-bind:src="game.get_image"> <!-- showing images of the games -->
                </figure>

                <h1 class="title">{{ game.name }}</h1> <!-- title of the game -->

                <p>
                <pre>{{ game.description }}</pre>
                </p> <!-- description of the game -->
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2> <!-- subtitle of information about the games -->

                <p><strong>Price per player:</strong> £{{ game.price }}</p>
                <!-- price of the game shown to users in bold -->

                <hr>
                <p>If you would like to bring another player such as your friend, add extra player to cart.
                </p>

                <!-- button and input fields for addToCart functionality -->
                <div class="field has-addons mt-6"> <!-- button and input will be into each other -->
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                        <!-- addToCart expects number, minimum of 1 game being added to the cart -->
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                        <!-- adds game user selected to the cart -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios' // to get games from the server we use axios to perform get requests to the server
import { toast } from 'bulma-toast' // pop up notifs to notify user when adding a game to the cart 

export default {
    name: 'Game',
    data() {
        return {
            game: {},
            quantity: 1 // default=1 and can't go below 1
        }
    },
    mounted() {
        this.getGame()
    },
    methods: {
        async getGame() {
            this.$store.commit('setIsLoading', true) // before axios finishes we set the 'setIsLoading' to true (for loading bar)

            const matches_slug = this.$route.params.matches_slug // geting matches slug from the url
            const game_slug = this.$route.params.game_slug // geting games slug from the url

            await axios
                .get(`/api/v1/games/${matches_slug}/${game_slug}`) // gets the games 
                .then(response => { // response back from the server
                    this.game = response.data

                    document.title = this.game.name + ' | Footy4U'
                })
                .catch(error => {
                    console.log(error) // logs errors to the console to fix/debug code
                })

            this.$store.commit('setIsLoading', false) // when axios finishes we set the 'setIsLoading' to false (for loading bar)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) { // checking whether if value of the quantity IS A NUMBER, if not set it to 1
                this.quantity = 1
            }

            const item = { // new item
                game: this.game, // set it to the game user is on
                quantity: this.quantity // referenced to quantity
            }

            this.$store.commit('addToCart', item) // calls store method in store/index.js line 28 and pass in variable item

            toast({ // notification
                message: 'Your booking has been added to the cart', // message to show to users
                type: 'is-success', // class = is-success (green colour)
                dismissible: true, // user can dismiss message
                pauseOnHover: true, // pauses when user hovers over the message
                duration: 2000, // 2000ms = 2 secs time of notification being shown to user
                position: 'bottom-right', // notification placed at bottom right of the screen
            })
        }
    }
}
</script>