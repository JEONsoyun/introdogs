<template>
  <div class="s-scrap-list">
    <template v-if="data != null && data.length != 0">
      <div
        @click="onDetailClick(dog.dog_id)"
        class="d-flex s-scrap-list-box"
        v-for="(dog, di) in data"
        :key="`dog-${di}`"
      >
        <div class="s-scrap-list-image" :style="`background-image: url(${dog.profile})`">
          <div class="s-scrap-list-heart">
            <v-icon color="red">favorite</v-icon>
          </div>
        </div>
        <div class="s-scrap-list-content">
          <div style="margin-bottom: 4px;">{{dog.dog_id}}</div>
          <div class="d-flex s-scrap-list-row">
            <div class="s-scrap-list-title">나이</div>
            <div class="s-scrap-list-text">{{dog.age}}</div>
          </div>
          <div class="s-scrap-list-bar" />
          <div class="d-flex s-scrap-list-row">
            <div class="s-scrap-list-title">성별</div>
            <div class="s-scrap-list-text">{{dog.sex == 'M' ? '남' : '여'}}</div>
          </div>
          <div class="s-scrap-list-bar" />
          <div class="d-flex s-scrap-list-row">
            <div class="s-scrap-list-title">견종</div>
            <div class="s-scrap-list-text">{{dog.kind}}</div>
          </div>
          <div class="s-scrap-list-bar" />
          <div class="d-flex s-scrap-list-row">
            <div class="s-scrap-list-title">털색</div>
            <div class="s-scrap-list-text">{{dog.color}}</div>
          </div>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="d-flex flex-column justify-center align-center">
        <img class="s-scrap-list-empty-image" src="/static/images/question_dog.png" />
        <div class="s-scrap-list-empty-text">관심 멍멍이 목록이 없네요!</div>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 's-scrap-list',
  props: {
    data: { type: Array, default: () => [] },
  },
  data: () => ({}),
  methods: {
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
  },
};
</script>

<style>
.s-scrap-list-box {
  width: 100%;
  margin-bottom: 24px;
  padding: 16px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
}

.s-scrap-list-image {
  position: relative;
  margin-right: 16px;
  height: 150px;
  width: 150px;
  background-size: cover;
  background-position: center center;
}

.s-scrap-list-heart {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.61);
  display: flex;
  justify-content: center;
  align-items: center;
}

.s-scrap-list-row {
  width: 100%;
  padding: 6px 0;
  display: flex;
  align-items: center;
}

.s-scrap-list-title {
  color: #ffd501;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.6px;
  margin-right: 10px;
  flex-shrink: 0;
}

.s-scrap-list-text {
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.48px;
  color: #616161;
}

.s-scrap-list-bar {
  width: 100%;
  border-bottom: solid 1px #eee;
}

.s-scrap-list-empty-image {
  margin-top: 24px;
  width: 220px;
  opacity: 0.4;
}

.s-scrap-list-empty-text {
  margin: 32px;
  font-size: 16px;
  color: #585858;
}
</style>