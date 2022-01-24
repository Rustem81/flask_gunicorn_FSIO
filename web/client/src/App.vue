<template>
  <div id="app" class="root">
    <button @click="getBE">
      <img src="./assets/logo.png" alt="" />
      GET BE
    </button>

    <h1>{{ notifications }}</h1>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "App",
  computed: {
    ...mapState({
      notifications: (state) => state.notifications,
    }),
  },
  methods: {
    getBE() {
      fetch(process.env.VUE_APP_TOCH)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          console.log(data);
        });
    },
  },
};
</script>
<style>
.root {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
