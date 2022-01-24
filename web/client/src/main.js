import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import VueSocketIOExt from "vue-socket.io-extended";
import { io } from "socket.io-client";

const socket = io(process.env.VUE_APP_PATH, {
  path: process.env.VUE_APP_SOCK,
});

console.log("socket");
console.log(socket);

Vue.use(VueSocketIOExt, socket, { store });
Vue.config.productionTip = false;

new Vue({
  store,
  render: (h) => h(App),
}).$mount("#app");
