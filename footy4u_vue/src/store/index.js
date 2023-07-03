import { createStore } from 'vuex'

export default createStore({
  state: { // states are variables/information
    cart: { // creating new object called cart
      items: [], // list of items
    },
    isAuthenticated: false, // able to add to cart even when user is not logged in or signed up
    token: '',
    isLoading: false // loading bar between games and adding games to the cart
  },
  mutations: { // synchronous to the variables 
    initializeStore(state) { // this is created to store things in the local storage of the browser
      if (localStorage.getItem('cart')) { // to check if local storage exists
        state.cart = JSON.parse(localStorage.getItem('cart')) // get object from local storage
      } else { // if it does not exist we create the local storage
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('token')) { // checks token in the local storage 
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true // if token is in the local storage we set to true for security purposes
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    addToCart(state, item) { // pass in item to add into the cart
      const exists = state.cart.items.filter(i => i.game.id === item.game.id) // checks if item exists in the cart

      if (exists.length) { // if exists is > 0 then it is certain that there is a game in the cart
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity) // gets the quantity from v-model="quantity" in Game.vue = Line 27
      } else { // if not in the cart we add into the cart
        state.cart.items.push(item) // 'push' to add game into the cart
      }

      localStorage.setItem('cart', JSON.stringify(state.cart)) // if we refresh browser everything will be stored 
    },
    setIsLoading(state, status) {
      state.isLoading = status // passes in false or true from one of the pages
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: [] } // clears the whole cart

      localStorage.setItem('cart', JSON.stringify(state.cart)) // removes cart from local storage
    }
  },
  actions: { // asynchronous functions to make changes
  },
  modules: {
  }
})
