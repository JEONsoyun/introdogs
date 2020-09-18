import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    ISLOGGEDIN: null,
    USER: {},

  },
  mutations: {
    ISLOGGEDIN(state, val) {
      state.ISLOGGEDIN = val
    },
    USER(state, val) {
      state.USER = val
    },

  },
  actions: {
  },
  modules: {
  },
  getters: {
    USER(state) {
      return state.USER;
    },
    ISLOGGEDIN(state) {
      return state.ISLOGGEDIN;
    }
  }
})
