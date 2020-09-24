<template>
  <s-first-layout title="잃어버린 멍멍이 찾기">
    <div class="lost-page">
      <div @click.stop="$refs.image.click">
        <s-button>
          <v-icon color="#fff">photo_camera</v-icon>
          <div style="margin-left:4px;">멍멍이 사진 업로드</div>
        </s-button>
        <input accept="image/*" class="d-none" ref="image" type="file" @input="pickFile" />
      </div>
      <div class="d-flex justify-center lost-page-image-container">
        <div
          class="lost-page-image"
          v-if="previewImage"
          :style="`background-image:url(${previewImage})`"
        />
      </div>
      <div class="d-flex" style="margin-top: 32px;">
        <v-text-field style="border-top-right-radius:0;border-bottom-right-radius:0;border-bottom-left-radius:0;" label="잃어버린 위치 검색" v-model="location" dense outlined solo flat hide-details></v-text-field>
        <div class="d-flex flex-grow-0">
          <s-button style="border-top-left-radius:0;border-bottom-left-radius:0;border-bottom-right-radius:0;">
            <v-icon color="#fff">search</v-icon>
          </s-button>
        </div>
      </div>
      <div class="lost-page-map">
        <s-map />
      </div>
      <s-button @click="onConfirmClick" style="margin-top: 32px;">입력 완료</s-button>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'lost-page',
  data: () => ({
    previewImage: null,
    location: '',
  }),
  methods: {
    pickFile(e) {
      let input = this.$refs.image;
      let file = input.files;
      if (file && file[0]) {
        let reader = new FileReader();
        reader.onload = (e) => (this.previewImage = e.target.result);
        reader.readAsDataURL(file[0]);
      } else {
        this.previewImage = null;
      }
    },
    onConfirmClick() {
      this.$router.push('/lost/result');
    },
  },
};
</script>

<style>
.lost-page {
  padding: 0 16px;
  padding-top: 64px;
  padding-bottom: 80px;
}

.lost-page-image-container {
  padding-top: 24px;
  max-width: 50%;
  height: 300px;
  display: flex;
  margin: 0 auto;
}

.lost-page-image {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
}

.lost-page input {
  padding: 0 !important;
}
.lost-page .v-input__control {
  height: 44px !important;
}

.lost-page .v-text-field__slot {
  height: 44px;
  font-size: 12px;
  color: #8a8a8a !important;
  
}
.lost-page fieldset {
  border-color: #ffd501 !important;
  height: 49px;
  border-bottom: 0;
}

.lost-page .v-text-field {
  font-size: 14px;
  font-weight: 400;
  letter-spacing: -0.39px;
  color: #c5c5c5;
}

.lost-page-map {
  border-bottom-right-radius: 4px;
  border-bottom-left-radius: 4px;
  overflow: hidden;
  border: solid 1px #ffd501;
  border-top: 0;
}
</style>