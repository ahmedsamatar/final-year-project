<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="Search"></h1>
                <h2 class="is-size">Search term: "{{ query }}"</h2>
                <!-- prints content for query variable defined in the data -->
            </div>

            <GameBox v-for="game in games" v-bind:key="game.id" v-bind:game="game" />
            <!-- loops through the games from the component 'GameBox.vue'  -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import GameBox from '@/components/GameBox.vue' // registering gamebox.vue

export default {
    name: 'Search',
    components: {
        GameBox
    },
    data() {
        return {
            games: [], // list of games
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Footy4U' // shows user which page currently on via the tab on browser

        let uri = window.location.search.substring(1) // gets the location of the search
        let params = new URLSearchParams(uri) // gets all the parameters based on the URL

        if (params.get('query')) { // getting query from the URL
            this.query = params.get('query') // set data query varible to the value of the query in the URL

            this.performSearch() // then executes the perform search method
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true) // loading bar set to true before axios gets executed

            await axios
                .post('api/v1/games/search/', { 'query': this.query }) // POST query back to the server 
                .then(response => {
                    this.games = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false) // loading bar set to false after axios gets executed
        }
    }
}
</script>