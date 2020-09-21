<template>
  <div class="d-flex justify-center align-center px-3 s-header">
    <v-icon @click="onMenuClick" color="#ffd501" size="24">menu</v-icon>
    <div class="d-flex" grow/>
    <!-- <img class="s-header-logo" @click="$router.push('/').catch(()=>{})" src="/static/images/스팟_로고_웹용@2x.png" /> -->
    <div @click="$router.push('/').catch(()=>{})">LOGO</div>
    <div class="d-flex" grow/>
    <v-icon @click="onMypageClick" color="#ffd501" size="30">person</v-icon>
  </div>
</template>

<script>
export default {
  name: 's-header',
  methods: {
    onMenuClick() {
      this.$emit("toggleMenu", true)
    },
    onMypageClick() {
      if (this.$store.state.ISLOGGEDIN) {
        return this.$router.replace('/login')
      }

      this.$emit("toggleMypage", true)
    }
  }
};
</script>

<style>
.s-header {
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: #fff;
}

.s-header-logo {
  height: 18px;
}
</style>
