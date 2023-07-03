<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Games #{{ order.id }}</h3> <!-- order title and id -->

        <h4 class="is-size-5">Games</h4>

        <table class="table is-fullwidth"> <!-- table showing different games -->
            <thead>
                <tr>
                    <th>Game</th>
                    <th>Price</th>
                    <th>Quantity (players)</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in order.items" v-bind:key="item.game.id"> <!-- loops through order items -->
                    <td>{{ item.game.name }}</td>
                    <td>£{{ item.game.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>£{{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderSummary',
    props: {
        order: Object // pass through the properties from OrderSummary
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.game.price // get item total
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => { // get total length of the order 
                return acc += curVal.quantity
            }, 0)
        },
        resetgameID(counter) {
            counter = counter + 1
            return counter
        }
    }
}
</script>