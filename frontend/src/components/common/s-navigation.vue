<template>
  <div class="s-navigation">
    <div class="d-flex align-center s-navigation-tabs">
      <div
        class="d-flex align-center justify-center s-navigation-tab"
        :class="{'s-navigation-tab--selected': selectedId==0}"
        @click="onNavigationClick(0)"
      >직관 투어</div>
      <div
        class="d-flex align-center justify-center s-navigation-tab"
        :class="{'s-navigation-tab--selected': selectedId==1}"
        @click="onNavigationClick(1)"
      >MY</div>
      <div
        class="d-flex align-center justify-center s-navigation-tab"
        :class="{'s-navigation-tab--selected': selectedId==2}"
        @click="onNavigationClick(2)"
      >우리 구단 TALK</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 's-navigation',
  data: () => ({
    selectedId: 0,
    naviArray: [
      { path: '/tour', id: 0 },
      { path: '/my/map', id: 1 },
      { path: '/talk', id: 2 },
    ],
  }),
  methods: {
    onNavigationClick(index) {
      if (index == 1 && !this.$store.state.USER.memberIdx) {
        alert('로그인이 필요합니다.');
        this.$router.push('/login');
        return;
      }
      const nextPath = this.naviArray.find((e) => e.id == index).path;

      if (this.$route.path == nextPath) {
        return;
      }

      this.selectedId = index;
      this.$router.push(nextPath);
    },
  },
  created() {
    let path = this.$route.path;
    let id = this.naviArray.find((e) => {
      if (path == '/my/dibs') {
        return e.path.includes('/my');
      }
      return path.includes(e.path);
    }).id;
    this.selectedId = id;
  },
};
</script>

<style lang="scss">
.s-navigation {
  background: #fff;
  z-index: 999;
  position: fixed;
  top: 48px;
  left: 0;
  right: 0;
}

.s-navigation-tabs {
  height: 40px;
}

.s-navigation-tab {
  width: 10px;
  height: 100%;
  border-bottom: solid 4px #fff;
  font-size: 14px;
  color: #585858;
  white-space: nowrap;
  font-weight: 700;
}

.s-navigation-tab--selected {
  border-bottom: solid 4px #61c5ff;
}
</style>