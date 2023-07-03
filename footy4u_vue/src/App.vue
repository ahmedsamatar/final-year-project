<template>
  <div id="wrapper"> <!-- wrap all contents to have one element in the template as it is required by Vue.js -->
    <nav class="navbar is-dark"> <!-- bulma class in use = menu at the top to give a dark theme -->
      <div class="navbar-brand"> <!-- logo -->
        <router-link to="/" class="navbar-item"><strong>Footy4U</strong></router-link> <!-- Nav bar to the home page which
        is on every page -->

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <!-- hamburger icon for small devices TALK ABOUT THIS ON THE PROJECT AS
          IT SHOWS THE APPLICATION TO BE SUPPORTED ON NUMEROUS DEVICES, when clicked on it calls the function !showMobileMenu -->
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a> <!-- three stripes in the burger icon -->
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <!-- bind attribute class to show isActive -->
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search"> <!-- from Vue get method on search functionality -->
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Search for Games!" name="query">
                  <!-- user input will be a text -->
                </div>

                <div class="control">
                  <button class="button is-success"> <!-- green coloured button for search -->
                    <span class="icon">
                      <i class="fas fa-search"></i> <!-- search icon -->
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end"> <!-- makes the other navigation links to the other side of the page -->
          <router-link to="/5-a-side" class="navbar-item">5-a-side</router-link>
          <!-- naivgation link to 5 a side pitches to view and book -->
          <router-link to="/7-a-side" class="navbar-item">7-a-side</router-link>
          <!-- naivgation link to 7 a side pitches to view and book -->
          <router-link to="/stats" class="navbar-item">Stats</router-link>
          <!-- naivgation link to Stats -->


          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <!-- this router link is displayed when my account is logged in -->
                <router-link to="/my-account" class="button is-light">My Account</router-link>
                <!-- navigation link to accounts page to view their bookings (ONLY APPEARS WHEN USER HAS LOGGED IN) -->
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
                <!-- navigation link to log in (ONLY APPEARS WHEN USER HAS NOT LOGGED IN/SIGNED UP) -->
                <router-link to="/sign-up" class="button is-light">Sign up</router-link>
                <!-- navigation link to sign up (ONLY APPEARS WHEN USER HAS NOT LOGGED IN/SIGNED UP) -->
              </template>

              <router-link to="/cart" class="button is-success">
                <!-- link to the cart to see which pitch you want to play on green colour -->
                <span class="icon"><i class="fas fa-shopping-cart"></i></span> <!-- shopping cart icon -->
                <span>Cart ({{ cartTotalLength }})</span>
                <!-- shows length of the cart in the menu which is a computed value -->
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
      <!-- loding bar functionality perfomed only when $store.state mentioned -->
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view /> <!-- all contents placed -->
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p> <!-- footer at bottom of the page -->
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false, // set to false to make sure it doesnt show mobile when opening the page 
      cart: { // to make cart avaiable in every page of the web app
        items: []
      }
    }
  },
  beforeCreate() { // makes sure store has been initialized
    this.$store.commit('initializeStore') // calls the mutations in store index.js

    const token = this.$store.state.token // get token from the state in local storage

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart // makes sure when user adds game to cart it updates synchronously 
  },
  computed: { // calculated variables based around the whole page 
    cartTotalLength() { // creating method, everytime cart changes this method updates
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) { // loop through all items in the cart 
        totalLength += this.cart.items[i].quantity // for each iteration of the loop
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma'; // importing bulma to style the page

// css for animated loaded bar while waiting information from the server

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
