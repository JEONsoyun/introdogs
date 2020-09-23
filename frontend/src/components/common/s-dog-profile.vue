<template>
  <div class="s-dog-profile-box">hi</div>
</template>

<script>
export default {
  name: 's-dog-profile',
  props: {
    data: { type: Object, default: () => ({}) },
  },
};
</script>

<style>
.s-dog-profile-box {
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
</style>