<template>
    <tr>
        <td>
            <RouterLink :to="item.game.get_absolute_url">{{ item.game.name }}</RouterLink> <!-- link to the games -->
        </td>
        <td>£{{ item.game.price }}</td> <!-- price of the game -->
        <td>
            {{ item.quantity }} <!-- quantity of games booked for the user -->
            <a @click="decrementQuantity(item)">-</a> <!-- user adding a player -->
            <a @click="incrementQuantity(item)">+</a> <!-- user removing a player -->
        </td>
        <td>£{{ getItemTotal(item).toFixed(2) }}</td> <!-- set to 2 decimal places -->
        <td><button class="delete" @click="removeFromCart(item)"></button></td> <!-- removing game from the cart -->
    </tr>
</template>

<script>


export default {
    name: "CartItem",
    props: {
        initialItem: Object // set to initial to make sure no changes to the item we are getting
    },
    data() {
        return {
            item: this.initialItem // sets the item to the property of the parent 
        };
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.game.price;
        },
        decrementQuantity(item) {
            item.quantity -= 1 // decrements quantity by 1 

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item) // if user decrements all then it would remove game from the cart
            }

            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1 // increments quanity by 1

            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart)) // stringify whole objects which is stored in the storage 
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item) // calls function back to the parent 

            this.updateCart()
        }
    },
}
</script>