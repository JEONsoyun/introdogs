<template>
  <div
    @click="onButtonClick"
    class="d-flex align-center justify-center s-button"
    :class="{
      's-button__white': type == 'white',
      's-button__gray': type == 'gray',
      's-button__small': type =='small'
    }"
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
  height: 44px;
  border-radius: 6px;
  background: #ffd501;
  color: #fff;
  font-weight: bold;
  letter-spacing: -0.16px;
  font-size: 16px;
  padding: 0 16px;
}

.s-button__white {
  height: 44px;
  border-radius: 6px;
  background: #fff;
  color: #ffd501;
  font-weight: bold;
  border: solid 1px #ffd501;
  letter-spacing: -0.16px;
  font-size: 16px;
  padding: 0 16px;
}

.s-button__gray {
  height: 44px;
  border-radius: 6px;
  background: #d2d2d2;
  color: #fff;
  font-weight: bold;
  letter-spacing: -0.16px;
  font-size: 16px;
  padding: 0 16px;
}

.s-button__small {
  height: 30px;
  border-radius: 6px;
  background: #ffd501;
  color: #fff;
  font-weight: bold;
  letter-spacing: -0.16px;
  font-size: 12px;
  padding: 0 12px;
}
</style>