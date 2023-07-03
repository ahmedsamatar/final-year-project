<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Footy4U
        </p>
        <p class="subtitle">
          Enjoy weekly/monthly football matches anywhere!
          <br>
          Engage in the Stats page in order to win prizes ranging from football shirts/boots to a premier league match
          ticket!
        </p>
      </div>
    </section>
    <div class="columns is-multiline"> <!-- has title and games next to each other -->
      <div class="column is-12"> <!-- fills up the screen -->
        <h2 class="is-size-2 has-text-centered">Latest Football Matches</h2>
        <!-- medium sized text in the centre of the page to make sure the latest games stay centred on the screen -->
      </div>
      <GameBox v-for="game in latestGames" v-bind:key="game.id" v-bind:game="game" />
      <!-- loops through the games from the component 'GameBox.vue'  -->
    </div>
  </div>
</template>

<script>
import axios from 'axios' // importing axios to API calls between frontend and backend 

import GameBox from '@/components/GameBox'

export default {
  name: 'Home',
  data() {
    return {
      latestGames: [] // empty list of the games 
    }
  },
  components: {
    GameBox // gets data components from GameBox.vue to reduce duplication of code
  },
  mounted() { // life cycles of Vue.js, when page is complete calls methods
    this.getLatestGames()

    document.title = 'Home | Footy4U' // shows user which page currently on via the tab on browser
  },
  methods: {
    async getLatestGames() { // gets the latest games from the backend 
      this.$store.commit('setIsLoading', true) // loading bar

      await axios
        .get('/api/v1/latest-games/') // calling api of latest games
        .then(response => { // response back from the server
          this.latestGames = response.data // list of objects
        })
        .catch(error => {
          console.log(error) // to show error in console
        })

      this.$store.commit('setIsLoading', false) // loading bar
    }
  }
}
</script>