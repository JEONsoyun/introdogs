<template>
  <s-main-layout title="관심 멍멍이 목록">
    <div class="scrap-page">
      <s-scrap-list :data="dogs" />
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'scrap-page',
  data: () => ({
    dogs: [],
  }),
  async created() {
    try {
      this.dogs = await this.$api.getScraps();
      console.log(this.dogs);
    } catch (e) {
      console.error(e);
    }
  },
};
</script>

<style>
.scrap-page {
  padding: 24px 16px;
}
</style>