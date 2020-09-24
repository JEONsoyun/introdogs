<template>
  <s-first-layout title="나와 어울리는 멍멍이 매칭">
    <div class="match-page-container">
      <div class="match-page-box">
        <div>1. 더 귀엽다고 생각하는 멍멍이를 선택해주세요.</div>
        <div style="margin-top:24px;">
          <div class="d-flex justify-center align-center match-page-number">1</div>
          <div class="d-flex">
            <div class="d-flex flex-column flex-grow-1 match-page-item">
              <div class="d-flex match-page-item-image" style="background:#eee"></div>
            </div>
            <div class="d-flex flex-column flex-grow-1 match-page-item">
              <div class="d-flex match-page-item-image" style="background:#eee"></div>
            </div>
            <div class="d-flex flex-column flex-grow-1 match-page-item">
              <div class="d-flex match-page-item-image" style="background:#eee"></div>
            </div>
          </div>
        </div>
        <div style="margin: 24px 0;width:100%;border-bottom: solid 1px #ffd501" />
        <div class="d-flex justify-center align-center match-page-number">2</div>
        <div class="d-flex">
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
        </div>
        <div style="margin: 24px 0;width:100%;border-bottom: solid 1px #ffd501" />
        <div class="d-flex justify-center align-center match-page-number">3</div>
        <div class="d-flex">
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
          <div class="d-flex flex-column flex-grow-1 match-page-item">
            <div class="d-flex match-page-item-image" style="background:#eee"></div>
          </div>
        </div>
      </div>
      <div class="match-page-box" style="margin-top: 24px;">
        <div>2. 해당사항에 체크해주세요.</div>
        <v-checkbox v-model="check1" color="#ffd501" hide-details label="나는 활동적인 편이다." />
        <v-checkbox v-model="check2" color="#ffd501" hide-details label="나는 금전적으로 여유가 있다." />
        <v-checkbox v-model="check3" color="#ffd501" hide-details label="나는 여가시간이 많은 편이다." />
      </div>
      <s-button @click="onResultClick" style="margin-top: 24px;">결과 보기</s-button>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'match-page',
  data: () => ({
    check1: false,
    check2: false,
    check3: false,
  }),
  methods: {
    onResultClick() {
      this.$router.push('/match/result');
    },
  },
};
</script>

<style>
.match-page-container {
  padding: 24px 12px;
  padding-top: 64px;
}

.match-page-box {
  width: 100%;
  padding: 16px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
}

.match-page-number {
  margin-left: 2px;
  margin-bottom: 8px;
  width: 28px;
  height: 28px;
  background: #ffd501;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  border-radius: 50%;
}

.match-page-item {
  width: 33%;
  min-height: 100px;
  height: 30vw;
  max-height: 200px;
}

.match-page-item-image {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  border: solid 3px #fff;
  border-radius: 8px;
}

.match-page-box .v-label {
  font-size: 12px;
}
</style>