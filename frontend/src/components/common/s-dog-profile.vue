<template>
  <div class="s-dog-profile-box">
    <div class="s-dog-profile-image" :style="`background-image: url(${data.profile})`" />
    <div class="s-dog-profile-content">
      <div style="padding: 0 16px;">{{data.dog_id}}</div>
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">나이</div>
          <div class="s-dog-profile-text">{{data.age}}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">성별</div>
          <div class="s-dog-profile-text">{{data.sex == 'M' ? '남' : '여'}}</div>
        </div>
      </div>
      <div class="s-dog-profile-bar" />
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">견종</div>
          <div class="s-dog-profile-text">{{data.kind}}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">털색</div>
          <div class="s-dog-profile-text">{{data.color}}</div>
        </div>
      </div>

      <div class="s-dog-profile-bar" />
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">무게</div>
          <div class="s-dog-profile-text">{{data.weight}}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">중성화 여부</div>
          <div class="s-dog-profile-text">{{data.neuter}}</div>
        </div>
      </div>
      <div class="s-dog-profile-bar" />
      <div class="d-flex s-dog-profile-row">
        <div class="s-dog-profile-title">특징</div>
        <div class="s-dog-profile-text">{{data.special}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 's-dog-profile',
  props: {
    data: { type: Object, default: () => ({}) },
  },
  data: () => ({
  }),
};
</script>

<style>
.s-dog-profile-box {
  width: 100%;
  padding-top: 16px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
}

.s-dog-profile-image {
  margin: 0 16px 16px 16px;
  height: 214px;
  background-size: cover;
  background-position: center center;
}

.s-dog-profile-row {
  width: 100%;
  padding: 12px 16px;
  min-height: 42px;
  display: flex;
  align-items: center;
}

.s-dog-profile-title {
  color: #ffd501;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.6px;
  margin-right: 10px;
  flex-shrink: 0;
}

.s-dog-profile-text {
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.48px;
  color: #616161;
}

.s-dog-profile-bar {
  width: 100%;
  border-bottom: solid 1px #eee;
}
</style>