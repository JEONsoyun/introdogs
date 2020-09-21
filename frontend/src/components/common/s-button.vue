<template>
  <div
    @click="onButtonClick"
    class="d-flex align-center justify-center s-button"
    :class="{'s-button__white': type == 'white',
    's-button__gray': type == 'gray'}"
  >
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    text: '',
    type: '',
  },
  methods: {
    onButtonClick() {
      this.$emit('click');
    },
  },
};
</script>

<style>
.s-button {
  width: 100%;
  height: 44px;
  border-radius: 6px;
  background: #ffd501;
  color: #fff;
  font-weight: bold;
  letter-spacing: -0.16px;
  font-size: 16px;
}

.s-button__white {
  width: 100%;
  height: 44px;
  border-radius: 6px;
  background: #fff;
  color: #ffd501;
  font-weight: bold;
  border: solid 1px #ffd501;
  letter-spacing: -0.16px;
  font-size: 16px;
}

.s-button__gray {
  width: 100%;
  height: 44px;
  border-radius: 6px;
  background: #d2d2d2;
  color: #fff;
  font-weight: bold;
  letter-spacing: -0.16px;
  font-size: 16px;
}
</style>