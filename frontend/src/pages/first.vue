<template>
  <s-first-layout>
    <div>
      <div></div>
      <div></div>
      <div style="padding: 0 32px;">
        <s-button type="small">Skip</s-button>
        <div class="d-flex">
          <div class="d-flex" />
          <v-checkbox v-model="check" style="padding: 0; margin: 0;" />
          <div>이 페이지 다시 안 보기</div>
        </div>
      </div>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  data: () => ({
    check: false,
  }),
};
</script>

<style>
</style>