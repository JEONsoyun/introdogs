<template>
  <s-first-layout>
    <div class="d-flex flex-column justify-center first-page-container">
      <div
        @click="$router.push('/match')"
        class="d-flex flex-column align-center justify-center first-page-item"
      >
        <img style="max-width: 50%;" src="/static/images/adopt_me.png" />
        <s-button style="margin-top:-8px;">나와 어울리는 멍멍이 매칭</s-button>
      </div>
      <div @click="$router.push('/lost')" class="d-flex flex-column align-center justify-center first-page-item">
        <img style="max-width: 50%" src="/static/images/lost_dog.png" />
        <s-button style="margin-top:-8px;">잃어버린 멍멍이 찾기</s-button>
      </div>
      <div class="d-flex flex-grow-0 first-page-check" style>
        <div class="d-flex align-center">
          <div class="d-flex" />
          <v-checkbox v-model="check" color="#ffd501" label="이 페이지 다시 안 보기" />
          <div class="d-flex flex-grow-0" style="margin-left: 12px;">
            <s-button @click="onSkipClick" type="white" size="small">Skip</s-button>
          </div>
        </div>
      </div>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'first-page',
  data: () => ({
    check: false,
  }),
  methods: {
    onSkipClick() {
      if (this.check) {
        localStorage.setItem('isChecked', true);
      } else {
        this.$store.commit('ISSKIP', true);
      }
      this.$router.push('/');
    },
  },
};
</script>

<style>
.first-page-container {
  height: 100%;
  padding: 32px 0;
}

.first-page-item {
  padding: 16px;
}

.first-page-check {
  margin-top: 32px;
  font-size: 12px;
  padding: 0 32px;
}

.first-page-check .v-label {
  font-size: 12px;
}
</style>