<template>
  <div class="d-flex s-dog-profile-small">
    <div
      class="d-flex flex-grow-0 s-dog-profile-small-image"
      :style="`background-image: url(${data.profile})`"
    >
      <div class="s-dog-profile-small-heart">
        <v-icon color="red">favorite</v-icon>
      </div>
    </div>
    <div class="d-flex flex-column flex-grow-1 s-dog-profile-small-content">
      <div style="margin-bottom: 4px;">{{data.dog_id}}</div>
      <div class="d-flex s-dog-profile-small-row">
        <div class="s-dog-profile-small-title">나이</div>
        <div class="s-dog-profile-small-text">{{data.age}}</div>
      </div>
      <div class="s-dog-profile-small-bar" />
      <div class="d-flex s-dog-profile-small-row">
        <div class="s-dog-profile-small-title">성별</div>
        <div class="s-dog-profile-small-text">{{data.sex == 'M' ? '남' : '여'}}</div>
      </div>
      <div class="s-dog-profile-small-bar" />
      <div class="d-flex s-dog-profile-small-row">
        <div class="s-dog-profile-small-title">견종</div>
        <div class="s-dog-profile-small-text">{{data.kind}}</div>
      </div>
      <div class="s-dog-profile-small-bar" />
      <div class="d-flex s-dog-profile-small-row">
        <div class="s-dog-profile-small-title">털색</div>
        <div class="s-dog-profile-small-text">{{data.color}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 's-dog-profile-small',
  props: {
    data: { type: Object, default: () => ({}) },
  },
  data: () => ({}),
  methods: {},
};
</script>

<style>
.s-dog-profile-small {
  width: 100%;
  padding: 16px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
}

.s-dog-profile-small-image {
  position: relative;
  margin-right: 16px;
  height: 150px;
  width: 150px;
  background-size: cover;
  background-position: center center;
}

.s-dog-profile-small-heart {
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

.s-dog-profile-small-row {
  width: 100%;
  padding: 6px 0;
  display: flex;
  align-items: center;
}

.s-dog-profile-small-title {
  color: #ffd501;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.6px;
  margin-right: 10px;
  flex-shrink: 0;
}

.s-dog-profile-small-text {
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.48px;
  color: #616161;
}

.s-dog-profile-small-bar {
  width: 100%;
  border-bottom: solid 1px #eee;
}

.s-dog-profile-small-empty-image {
  margin-top: 24px;
  width: 220px;
  opacity: 0.4;
}

.s-dog-profile-small-empty-text {
  margin: 32px;
  font-size: 16px;
  color: #585858;
}
</style>