import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    session_id: 0
  },
  getters: {
    baseUrlBackEnd: () => "http://127.0.0.1:5000/"
  },
  mutations: {
    connect(state, student) {
      state.session_id = student
    },
    disconnect(state) {
      state.session_id = 0
    }
  },
  actions: {
  },
  modules: {
  }
})
