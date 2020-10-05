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
    dogs: [],
    isScrapped: false,
  }),
  methods: {
    onScrapClick() {
      if (!this.$store.state.ISLOGGEDIN) {
        alert('로그인 후 사용 가능합니다.');
        return;
      }
      this.isScrapped = !this.isScrapped;
      if (this.isScrapped) {
        this.postScrap();
      } else {
        this.deleteScrap();
      }
    },
    async postScrap() {
      try {
        await this.$api.postScrap({ dog_id: this.dogId });
      } catch (e) {
        console.error(e);
      }
    },
    async deleteScrap() {
      try {
        await this.$api.deleteScrap(this.dogId);
      } catch (e) {
        console.error(e);
      }
    },
    async getScraps() {
      try {
        let res = await this.$api.getScraps();
        this.dogs = res.user[0].dog_info;
        for (let i in this.dogs) {
          if (this.dogs[i].dog_id == this.dogId) {
            this.isScrapped = true;
            this.$forceUpdate();
            return;
          }
        }
      } catch (e) {
        console.error(e);
      }
    },
    async getDog() {
      try {
        let res = await this.$api.getDog(this.dogId);
        this.dog = res.dog_info[0];
      } catch (e) {
        console.error(e);
        alert('잘못된 접근입니다.');
        this.$router.push('/');
      }
    },
  },
  async created() {
    this.dogId = this.$route.params.id;
    if (this.dogId == 0) {
      alert('잘못된 접근입니다.');
      this.$router.push('/');
    }
    await this.getScraps();
    this.getDog();
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