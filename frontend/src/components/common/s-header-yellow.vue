<template>
  <div class="d-flex justify-center align-center px-3 s-header-yellow">
    <v-icon style="width:26px" @click="onMenuClick" color="#fff" size="24">menu</v-icon>
    <div class="d-flex" grow/>
    <img class="s-header-yellow-logo" @click="$router.push('/first').catch(()=>{})" src="/static/images/logo.png" />
    <div class="d-flex" grow/>
    <v-icon style="width:26px" @click="onMypageClick" color="#fff" size="30">person</v-icon>
  </div>
</template>

<script>
export default {
  name: 's-header-yellow',
  methods: {
    onMenuClick() {
      this.$emit("toggleMenu", true)
    },
    onMypageClick() {
      if (!this.$store.state.ISLOGGEDIN) {
        return this.$router.replace('/login')
      }

      this.$emit("toggleMypage", true)
    }
  }
};
</script>

<style>
.s-header-yellow {
  z-index: 999;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: #ffd501;
}

.s-header-yellow-logo {
  height: 22px;
  cursor: pointer;
}
</style>
