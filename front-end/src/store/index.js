import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    connected: false
  },
  getters: {
    baseUrlBackEnd: () => "http://127.0.0.1:5000/"
  },
  mutations: {
    connection (state) {
      state.connected = !state.connected
    }
  },
  actions: {
    connection (context) {
      context.commit("connection")
    }
  },
  modules: {}
})

