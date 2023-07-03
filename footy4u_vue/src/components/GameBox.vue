<template>
    <!-- used to reuse code throughout the application -->
    <div class="column is-3"> <!--  -->
        <div class="box"> <!-- shadow around the game that has been listed -->
            <figure class="image mb-4"> <!-- image of the game you want to play -->
                <img :src="game.get_thumbnail"> <!-- whole url to the image -->
            </figure>
            <h3 class="is-size-4">{{ game.name }}</h3> <!-- name of the game -->
            <p class="is-size-6 has-text-grey">£{{ game.price }}</p> <!-- price of the game -->

            <router-link v-bind:to="game.get_absolute_url" class="button is-dark mt-4">View Game
                Details</router-link>
            <!-- router link binded to the absolute url of a game, button dark and has spacing between image and text -->
        </div>
    </div>
</template>

<script>
export default {
    name: 'GameBox',
    props: {
        game: Object // passes information from the parent down to the component using props
    }
}
</script>
<!-- to remove spaces around the image to make image more clear -->
<style scoped>
.image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
}
</style>
