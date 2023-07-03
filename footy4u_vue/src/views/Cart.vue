<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box"> <!-- shadowed contents -->
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <!-- table that fills up the page and will ONLY SHOW IF THERE IS GAMES IN THE CART -->
                    <thead>
                        <tr>
                            <th>Game</th>
                            <th>Price</th>
                            <th>Quantity (players)</th>
                            <th>Total</th>
                            <th>Remove from Cart</th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem v-for="item in cart.items" v-bind:key="item.game.id" v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                        <!-- loops through cart.items, listens to remove from cart -->
                    </tbody>
                </table>
                <p v-else>You don't have any games in your cart...</p> <!-- no games in the cart will display this text -->
            </div>
            <div class="column is-12 box"> <!-- shadowed content -->
                <h2 class="subtitle">Summary</h2>
                <strong>£{{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} Games/Players
                <!-- new computed value to show total price with the amount in the cart -->
                <hr>
                <RouterLink to="/cart/checkout" class="button is-dark">Proceed to checkout</RouterLink>
                <!-- button in order to proceed to checkout -->
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import CartItem from '@/components/CartItem.vue'; // importing CartItem
export default {
    name: 'Cart',
    components: {
        CartItem // inheriting the properties from CartItem
    },
    data() {
        return {
            cart: {
                items: [] // setting empty list for code not to crash
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart // makes sure when user adds game to cart it updates synchronously 

        document.title = 'Cart | Footy4U' // shows user which page currently on via the tab on browser
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.game.id !== item.game.id) // filters out the game user recieves and removes it from the cart
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

