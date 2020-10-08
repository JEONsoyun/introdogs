<template>
  <s-main-layout title="나와 닮은 멍멍이">
    <div class="my-similar-page">
      <template v-if="dog != null && dog.id != null">
        <s-dog-profile :data="dog" />
        <s-button @click="onDetailClick(dog.dog_id)" style="margin-top: 24px"
          >더 자세히 보기</s-button
        >
        <s-button
          @click="$router.push('/similar')"
          type="white"
          style="margin-top: 12px"
          >다시 찾아보기</s-button
        >
      </template>
      <template v-else>
        <div class="d-flex flex-column justify-center align-center">
          <img
            class="my-similar-page-empty-image"
            src="/static/images/question_dog.png"
          />
          <div class="my-similar-page-empty-text">
            나와 닮은 멍멍이 기록이 없네요!
          </div>
        </div>
        <s-button @click="$router.push('/similar')" style="margin-top: 24px"
          >나와 닮은 멍멍이 찾으러 가기</s-button
        >
      </template>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'my-similar-page',
  data: () => ({
    dogId: null,
    dog: {},
  }),
  methods: {
    async getMe() {
      try {
        let res = await this.$api.getMe();
        this.dogId = res.user[0].same_dog;
        console.log(this.dogId);
      } catch (e) {
        if (!e || !e.response || e.response.status != 400) {
          console.error(e);
        }
      }
    },
    async getDog() {
      let res = await this.$api.getDog(this.dogId);
      console.log(res);
      this.dog = res.dog_info[0];
      try {
      } catch (e) {
        console.error(e);
      }
    },
    onDetailClick() {
      this.$router.push(`/detail/${this.dogId}`);
    },
  },
  async created() {
    await this.getMe();
    if (this.dogId) {
      this.getDog();
    }
  },
};
</script>

<style>
.my-similar-page {
  padding: 24px 12px;
}

.my-similar-page-empty-image {
  margin-top: 24px;
  width: 220px;
  opacity: 0.4;
}

.my-similar-page-empty-text {
  margin: 32px;
  font-size: 16px;
  color: #585858;
}
</style>