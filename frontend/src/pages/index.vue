<template>
  <s-main-layout>
  </s-main-layout>
</template>

<script>
export default {
  name: 'index',
  data: () => ({
  }),
  methods: {
    // async getBest(cnt) {
    //   try {
    //     if (cnt != 0) {
    //       this.cnt += cnt;
    //     }
    //     let temp = await this.$api.getBest(this.startNum, this.cnt);
    //     this.best = temp;
    //     for (let i = 0; i < this.best.length; i++) {}
    //   } catch (e) {
    //     console.error(e);
    //   }
    // }
  },
  async created() {
    // this.getBest(0);
  },
};
</script>

<style>
</style>

