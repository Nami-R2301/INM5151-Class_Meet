import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    session_id: 0,
    student: {
      id: 0,
      username: "",
      email: ""
    }
  },
  getters: {
    baseUrlBackEnd: () => "http://127.0.0.1:5000/"
  },
  mutations: {
    connect(state, student) {
      state.student = student
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
