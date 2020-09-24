<template>
  <div class="s-map">
    <div class="s-map-map"></div>
    <template v-if="!noList">
      <div class="s-map-list"></div>
    </template>
  </div>
</template>

<script>
export default {
  name: 's-map',
  props: {
    noList: {type: Boolean, default: false},
  },
};
</script>

<style>
.s-map {
  width: 100%;
}

.s-map-map {
  width: 100%;
  min-height: 180px;
  height: 50vw;
  max-height: 320px;
  background: #eee;
}

.s-map-list {
  min-height: 160px;
  height: 30vw;
  max-height: 240px;
  background: #fff;
}
</style>