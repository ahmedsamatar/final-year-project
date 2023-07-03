<template>
    <div class="page-matches">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ matches.name }}</h2> <!-- title of the matches -->
            </div>
            <GameBox v-for="game in matches.games" v-bind:key="game.id" v-bind:game="game" />
            <!-- loops through the games from the component 'GameBox.vue'  -->
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import GameBox from '@/components/GameBox' // import properties from GameBox.vue
export default {
    name: 'Matches',
    components: {
        GameBox // gets data components from GameBox.vue to reduce duplication of code
    },
    data() {
        return {
            matches: {
                games: []
            }
        }
    },
    mounted() {
        this.getMatches() // getting the matches from the backend
    },
    watch: { // watches changes of the router in the URL
        $route(to, from) {
            if (to.name === 'Matches') { // if to == matches then it performs the mounted fuction
                this.getMatches()
            }
        }
    },
    methods: {
        async getMatches() {
            const matchesSlug = this.$route.params.matches_slug // gets category slug from the route paramter

            this.$store.commit('setIsLoading', true) // loading bar 

            axios
                .get(`api/v1/games/${matchesSlug}/`) // route to the matches
                .then(response => {
                    this.matches = response.data // gets the matches as well as the games together 

                    document.title = this.matches.name + ' | Footy4U' // shows user which page currently on via the tab on browser
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.', // error message displayed
                        type: 'is-danger', // red colour information
                        dismissible: true, // user can dismiss message
                        pauseOnHover: true, // pauses when user hovers over the message
                        duration: 2000, // 2000ms = 2 secs time of notification being shown to user
                        position: 'bottom-right', // notification placed at bottom right of the screen
                    })
                })

            this.$store.commit('setIsLoading', false) // loading bar set to false after axios is completed
        }
    }
}
</script>