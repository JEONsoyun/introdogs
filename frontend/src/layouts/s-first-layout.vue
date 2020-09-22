<template>
  <div class="d-flex flex-column">
    <div class="s-first-layout-header-container">
      <div class="d-flex align-center s-first-layout-header">LOGO</div>
    </div>
    <div class="s-first-layout-content">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 's-first-layout',
  data: () => ({}),
  methods: {},
};
</script>

<style>
.s-first-layout {
  padding-top: 40px;
}

.s-first-layout-header-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 10;
}

.s-first-layout-header {
  position: relative;
  height: 48px;
  background: #fff;
  font-size: 14px;
  font-weight: 700;
  color: #585858;
  border-bottom: solid 1px #e9e9e9;
}

.s-first-layout-content {
  position: relative;
  padding-top: 48px;
  min-height: 100vh;
  background-color: #fbfbfb;
}
</style>