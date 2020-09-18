<template>
  <!-- <div id="app" v-if="isLoggedIn != null"> -->
  <div id="app">
    <router-view />
  </div>
</template>

<script>
// Login check
const prohibitedContextsBeforeLoggedIn = [
  /^\/info/,
]

export default {
  name: 'App',
  data: () => ({
    isLoggedIn: null,
    allowedBeforeLoggedInContext: [

    ],
  }),
  async beforeCreate() {
    // try {
    //   let { data: [ user ] } = await this.$api.getMe();
    //   this.$store.commit('USER', user);
    // } catch (e) {
    //   if (!e || !e.response || e.response.status != 400) {
    //     console.error(e);
    //   }
    //   this.$store.commit('USER', {});
    // }

    // try {
    //   this.isLoggedIn = await this.$api.isLoggedIn();
    //   this.$store.commit('ISLOGGEDIN', this.isLoggedIn);
    // } catch (e) {
    //   console.log(e);
    //   this.isLoggedIn = false
    //   this.$store.commit('ISLOGGEDIN', false);
    // }

    // if (!this.isLoggedIn) {
    //   for (const context of prohibitedContextsBeforeLoggedIn) {
    //     if (this.$route.path.match(context)) {
    //       return this.$router.replace('/login')
    //     }
    //   }
    // }

    // window.$root = this
    // console.log(this.$store.getters.ISLOGGEDIN)
  },
};
</script>

<style>
.v-overlay__scrim {
  z-index: 1000 !important;
}

span {
  margin: 0 !important;
}
</style>
