import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notifications: [],
  },
  mutations: {
    SOCKET_LOG_MESSAGES(state, message) {
      console.log(message.text);
      state.notifications.push(message.text);
    },
  },
  actions: {
    socket_logMessage(vuexContext, message) {
      vuexContext.commit("SOCKET_LOG_MESSAGES", message);
    },
  },

  modules: {},
});
