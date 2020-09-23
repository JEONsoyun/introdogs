<template>
  <v-navigation-drawer
    :width="300"
    class="d-flex flex-column s-navigation-drawer-container"
    v-model="mDrawer"
    fixed
    temporary
    touchless
    :overlay-opacity="0.25"
    style="z-index:9999"
  >
    <div class="s-navigation-drawer-header">
      <v-icon @click="onToggleEvent" color="#ffd501" size="26">close</v-icon>
    </div>

    <div class="d-flex flex-column">
      <div class="d-flex">
        <div
          @click="onMenuClick(1)"
          class="d-flex align-center s-navigation-drawer-menu"
          :class="{'s-navigation-drawer-menu--selected': selectedMenuId == 1}"
        >
          <v-icon size="24" style="margin-right:8px;">location_on</v-icon>
          <div>내 주변 멍멍이 찾기</div>
        </div>
      </div>
      <div class="d-flex">
        <div
          @click="onMenuClick(1)"
          class="d-flex align-center s-navigation-drawer-menu"
          :class="{'s-navigation-drawer-menu--selected': selectedMenuId == 1}"
        >
          <v-icon size="24" style="margin-right:8px;">face</v-icon>
          <div>나와 닮은 멍멍이 찾기</div>
        </div>
      </div>
      <div class="s-navigation-drawer-bar" />
      <div class="d-flex">
        <div
          @click="onMenuClick(1)"
          class="d-flex align-center s-navigation-drawer-menu"
          :class="{'s-navigation-drawer-menu--selected': selectedMenuId == 1}"
        >
          <v-icon size="24" style="margin-right:8px;">accessibility_new</v-icon>
          <div>나와 어울리는 멍멍이 매칭</div>
        </div>
      </div>
      <div class="d-flex">
        <div
          @click="onMenuClick(1)"
          class="d-flex align-center s-navigation-drawer-menu"
          :class="{'s-navigation-drawer-menu--selected': selectedMenuId == 1}"
        >
          <v-icon size="24" style="margin-right:8px;">search</v-icon>
          <div>잃어버린 멍멍이 찾기</div>
        </div>
      </div>
      <div class="s-navigation-drawer-bar" />
      <div class="d-flex">
        <div
          @click="onMenuClick(0)"
          class="d-flex align-center s-navigation-drawer-menu"
          :class="{'s-navigation-drawer-menu--selected': selectedMenuId == 0}"
        >
          <v-icon size="24" style="margin-right:8px;">pets</v-icon>
          <div>ABOUT</div>
        </div>
      </div>
    </div>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 's-navigation-drawer',
  props: {
    drawer: { type: Boolean, default: false },
  },
  data() {
    return {
      items: [
        { title: 'About' },
        { title: '공지사항 및 이용약관' },
        { title: '고객센터' },
      ],
      pathArray: [
        { id: 0, path: '/about' },
        { id: 1, path: '/notice' },
        { id: 2, path: '/center' },
      ],
      selectedMenuId: null,
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
    onToggleEvent() {
      this.$emit('toggleMenu', false);
    },
    onMenuClick(index) {
      this.selectedMenuId = index;
      this.onToggleEvent();
      this.$router.push(
        this.pathArray.find((e) => {
          return e.id == this.selectedMenuId;
        }).path
      );
    },
  },
  created() {
    let path = this.$route.path;
    for (let i = 0; i < this.pathArray.length; ++i) {
      if (path == this.pathArray[i].path) {
        this.selectedMenuId = this.pathArray[i].id;
        break;
      }
    }
  },
};
</script>

<style>
.s-navigation-drawer-container {
  background: #000;
  padding-left: 20px;
}

.s-navigation-drawer-header {
  padding: 16px;
  padding-left: 0;
  margin-left: -6px;
}

.s-navigation-drawer-bar {
  margin-top: 32px;
  border-top: solid 2px rgb(238, 238, 238);
}

.s-navigation-drawer-menu {
  padding: 32px 8px 0 0;
  font-weight: 800;
  color: #686868;
  font-size: 18px;
  line-height: 23px;
}

.s-navigation-drawer-menu--selected {
  color: #ffd501;
}
</style>
