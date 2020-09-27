<template>
  <div class="mobile-layout-container">
    <div class="d-flex flex-column mobile-layout" :class="{'s-main-layout': title != ''}">
      <s-header
        @toggleMenu="onToggleEvent($event, 'navigationDrawer')"
        @toggleMypage="onToggleEvent($event, 'mypageDrawer')"
      />
      <s-navigation-drawer
        @toggleMenu="onToggleEvent($event, 'navigationDrawer')"
        :drawer="navigationDrawer"
      />
      <s-mypage-drawer
        @toggleMypage="onToggleEvent($event, 'mypageDrawer')"
        :drawer="mypageDrawer"
      />
      <div class="s-main-layout-content">
        <div class="s-main-layout-header-container">
          <div class="d-flex justify-center align-center s-main-layout-header" v-if="title != ''">
            <div
              v-if="!noArrow"
              @click="$router.go(-1)"
              class="d-flex justify-center align-center s-main-layout-header-arrow"
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
</template>

<script>
export default {
  name: 's-main-layout',
  props: {
    title: { type: String, default: '' },
    noArrow: Boolean,
  },
  data: () => ({
    navigationDrawer: false,
    mypageDrawer: false,
  }),
  methods: {
    onToggleEvent(drawer, target) {
      this[target] = drawer;
    },
  },
};
</script>

<style>
.s-main-layout {
  padding-top: 40px;
}

.s-main-layout-content {
  position: relative;
  padding-top: 48px;
  min-height: 100vh;
  background-color: #fbfbfb;
}

.s-main-layout-header-container {
  position: fixed;
  top: 48px;
  left: 0;
  width: 100%;
  z-index: 10;
}

.s-main-layout-header {
  position: relative;
  height: 40px;
  background: #fff;
  font-size: 14px;
  font-weight: 700;
  color: #585858;
  border-bottom: solid 1px #e9e9e9;
}

.s-main-layout-header-arrow {
  position: absolute;
  top: 6px;
  left: 10px;
}
</style>