<template>
  <s-main-layout title="멍멍이 상세보기">
    <div class="detail-page">
      <div class="d-flex align-center" style="margin-bottom: 8px">
        <div class="detail-page-title">{{ dog ? dog.dog_id : '' }}</div>
        <div class="d-flex" />
        <div @click="onScrapClick">
          <v-icon v-if="isScrapped" size="36" color="red">favorite</v-icon>
          <v-icon v-if="!isScrapped" size="36" color="red"
            >favorite_border</v-icon
          >
        </div>
      </div>
      <s-dog-profile :data="dog" isDetail />
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'detail-page',
  data: () => ({
    dogId: 0,
    dog: {},
    isScrapped: false,
  }),
  methods: {
    onScrapClick() {
      this.isScrapped = !this.isScrapped;
    },
  },
  async created() {
    this.dogId = this.$route.params.id;
    if (this.dogId == 0) {
      this.dogId = 'N448538202000489';
    }
    // dog api 부르기
    try {
      let res = await this.$api.getDog(this.dogId);
      this.dog = res.dog_info[0];
      console.log(this.dog);
    } catch (e) {
      console.error(e);
    }
  },
};
</script>

<style>
.detail-page {
  padding: 24px 16px;
  padding-bottom: 80px;
}

.detail-page-title {
  font-size: 16px;
  letter-spacing: -0.48px;
  font-weight: bold;
}
</style>