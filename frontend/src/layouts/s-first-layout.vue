<template>
  <div class="mobile-layout-container">
    <div class="mobile-layout">
      <div class="d-flex flex-column">
        <div class="s-first-layout-header-container">
          <div @click="$router.push('/')" class="d-flex align-center s-first-layout-header">LOGO</div>
        </div>
        <div class="s-first-layout-content">
          <div class="s-first-layout-sub-container">
            <div class="d-flex justify-center align-center s-first-layout-sub" v-if="title != ''">
              <div
                v-if="!noArrow"
                @click="$router.go(-1)"
                class="d-flex justify-center align-center s-first-layout-sub-arrow"
              >
                <v-icon size="28" color="#ffd501">keyboard_arrow_left</v-icon>
              </div>
              <div>{{title}}</div>
            </div>
          </div>
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 's-first-layout',
  props: {
    title: { type: String, default: '' },
    noArrow: Boolean,
  },
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

.s-first-layout-sub-container {
  position: fixed;
  top: 48px;
  left: 0;
  width: 100%;
  z-index: 10;
}

.s-first-layout-sub {
  position: relative;
  height: 40px;
  background: #fff;
  font-size: 14px;
  font-weight: 700;
  color: #585858;
  border-bottom: solid 1px #e9e9e9;
}

.s-first-layout-sub-arrow {
  position: absolute;
  top: 6px;
  left: 10px;
}
</style>