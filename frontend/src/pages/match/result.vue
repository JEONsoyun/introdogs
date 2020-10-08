<template>
  <s-first-layout title="멍멍이 매칭 결과">
    <div class="match-result-page">
      <template v-if="loading">
        <div class="d-flex justify-center align-center">
          <img
            style="margin-top: 70px; width: 60vw; max-width: 300px"
            src="/static/images/loading.gif"
          />
        </div>
        <div
          style="
            margin-top: 48px;
            margin-bottom: 60px;
            font-size: 16px;
            letter-space: -0.4px;
            font-weight: 700;
            text-align: center;
            color: #585858;
          "
        >
          나와 닮은 멍멍이를 찾고있어요!<br />최대 1분의 시간이 소요될 수
          있습니다.
        </div>
      </template>
      <template v-else>
        <template v-if="result">
          <s-dog-profile :data="dog" />
          <s-button @click="onDetailClick(dog.dog_id)" style="margin-top: 24px"
            >더 자세히 보기</s-button
          >
          <s-button
            @click="$router.push('/')"
            type="white"
            style="margin-top: 12px"
            >다른 멍멍이들 보러 가기</s-button
          >
        </template>
        <template v-else>
          <div class="d-flex justify-center align-center">
            <img
              style="margin-top: 40px; width: 40vw; max-width: 300px"
              src="/static/images/warning.png"
            />
          </div>
          <div
            style="
              margin: 24px 0;
              font-size: 16px;
              letter-space: -0.4px;
              font-weight: 700;
              text-align: center;
              color: #585858;
            "
          >
            [매칭 결과]<br /><br />아직 멍멍이를 맞이할 준비가 되지 않은
            사용자입니다!<br />
            입양에 대해 조금 더 고려한 후에,<br />
            매칭을 다시 시도해주세요.
          </div>
          <s-button
            @click="$router.push('/first')"
            type="white"
            style="margin-top: 24px"
            >첫 화면으로 가기</s-button
          >
          <s-button @click="onMainClick" style="margin-top: 12px"
            >메인으로 가기</s-button
          >
        </template>
      </template>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'match-result-page',
  data: () => ({
    dog: {},
    q: null,
    result: null,
    loading: true,
  }),
  methods: {
    onMainClick() {
      this.$store.commit('ISSKIP', true);
      this.$router.push('/');
    },
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
    async postMatch() {
      try {
        let res = await this.$api.postMatch({
          pick: this.q.pick,
          survey: this.q.survey,
        });
        console.log(res);
        this.result = res.data.qualification;
        if (this.result) {
          this.dog = res.data.list[0];
        }
      } catch (e) {
        console.error(e);
      }
      this.loading = false;
    },
  },
  created() {
    this.q = this.$route.query;
    console.log(this.q);
    if (this.q.pick[0] == '[') {
      alert('잘못된 접근입니다. 다시 시도해주세요.');
      this.$router.push('/');
    }

    this.postMatch();
  },
};
</script>

<style>
.match-result-page {
  padding: 24px 12px;
  padding-bottom: 60px;
}
</style>