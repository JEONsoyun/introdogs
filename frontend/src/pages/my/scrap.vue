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
      let res = await this.$api.getScraps();
      this.dogs = res.user[0].dog_info;
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