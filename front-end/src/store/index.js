import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    session_id: 0
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
