<template>
  <v-navigation-drawer
    :width="300"
    class="d-flex flex-column s-mypage-drawer-container"
    v-model="mDrawer"
    fixed
    temporary
    touchless
    :overlay-opacity="0.25"
  >
    <div class="d-flex flex-grow-0 s-mypage-drawer-header">
      <div class="d-flex" />
      <v-icon @click="onToggleEvent" color="#ffd501" size="26">close</v-icon>
    </div>
    <div class="d-flex flex-grow-0 align-center">
      <div class="d-flex flex-grow-0 justify-center align-center s-mypage-drawer-img">
        <img style="max-width: 80%" src="/static/images/dog_profile.png" />
      </div>
      <div class="s-mypage-drawer-id">{{$store.state.USER.memberName || '사용자ID'}}</div>
    </div>
    <div class="s-mypage-drawer-bar" />
    <div class="d-flex flex-column flex-grow-1 s-mypage-drawer-menu-container">
      <template v-for="(menu, menuIndex) in items">
        <div
          @click="onMenuClick(menu.path)"
          class="s-mypage-drawer-menu"
          :key="menuIndex"
        >{{menu.title}}</div>
        <div class="s-mypage-drawer-bar" :key="`${menuIndex}-bar`" />
      </template>
    </div>
    <div class="d-flex flex-column s-mypage-drawer-footer">
      <s-button @click="onLogoutClick" type="gray">로그아웃</s-button>
    </div>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 's-mypage-drawer',
  props: {
    drawer: { type: Boolean, default: false },
  },
  data() {
    return {
      items: [
        { title: '관심 멍멍이 목록', path: '/my/scrap' },
        { title: '나와 닮은 멍멍이', path: '/my/similar' },
      ],
      mDrawer: this.drawer,
    };
  },
  watch: {
    drawer(val) {
      this.mDrawer = val;
    },
    mDrawer(val) {
      if (!val) {
        this.onToggleEvent();
      }
    },
  },
  methods: {
    onProfileClick() {
      if (!this.$route.path.match(/^\/info/)) {
        this.$router.push('/info');
      } else {
        this.$emit('toggleMypage', false);
      }
    },
    onToggleEvent() {
      this.mDrawer = false;
      this.$emit('toggleMypage', false);
    },
    onMenuClick(path) {
      this.onToggleEvent();
      let cpath = this.$route.path;
      if (cpath != path) {
        this.$router.push(path);
      }
    },
    async onLogoutClick() {
      try {
        await this.$api.logout();
        location.href = '/tour';
      } catch (e) {
        console.error(e);
      }
    },
    created() {
      const user = this.$store.state.USER;
      this.user.memberName = user.memberName;
    },
  },
};
</script>

<style>
.s-mypage-drawer-container {
  background: #000;
  z-index: 9999;
  width: 100% !important;
}

.s-mypage-drawer-container .v-navigation-drawer__content {
  display: flex;
  flex-direction: column;
}

.s-mypage-drawer-header {
  padding: 10px 10px 0 10px;
}

.s-mypage-drawer-img {
  margin: 0 20px 20px 20px;
  width: 78px;
  height: 78px;
  border: solid 2px #ffd501;
  border-radius: 50%;
  background: #fff;
  overflow: hidden;
}

.s-mypage-drawer-id {
  margin-bottom: 20px;
  font-size: 18px;
  line-height: 18px;
  letter-spacing: -0.36px;
  color: #1e1e1e;
  font-weight: 800;
}

.s-mypage-drawer-menu-container {
  background: #fbfbfb;
}

.s-mypage-drawer-bar {
  border-top: solid 1px rgb(234, 234, 234);
  width: 100%;
}

.s-mypage-drawer-button {
  margin: 12px;
  height: 35px;
  background: #ffd501;
  color: #fff;
  font-size: 16px;
  line-height: 18px;
  letter-spacing: -0.16px;
  border-radius: 2px;
}

.s-mypage-drawer-menu {
  color: #404040;
  font-weight: 700;
  font-size: 16px;
  padding: 18px 20px;
}

.s-mypage-drawer-footer {
  border-top: solid 1px rgb(234, 234, 234);
  background: #fbfbfb;
  padding: 12px;
}

.s-mypage-drawer-button-gray {
  margin: 12px;
  height: 35px;
  background: #d2d2d2;
  color: #fff;
  font-size: 16px;
  line-height: 18px;
  letter-spacing: -0.16px;
  border-radius: 2px;
}
</style>
