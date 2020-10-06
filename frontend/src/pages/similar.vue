<template>
  <s-main-layout title="나와 닮은 멍멍이 찾기">
    <div class="my-similar-page">
      <div @click.stop="$refs.image.click">
        <s-button>
          <v-icon color="#fff">photo_camera</v-icon>
          <div style="margin-left: 4px">내 사진 업로드</div>
        </s-button>
        <input
          accept="image/*"
          class="d-none"
          ref="image"
          type="file"
          @input="pickFile"
        />
      </div>
      <div class="d-flex justify-center my-similar-page-image-container">
        <div
          class="my-similar-page-image"
          v-if="previewImage"
          :style="`background-image:url(${previewImage})`"
        />
      </div>
      <s-button
        v-if="previewImage"
        @click="onConfirmClick(1)"
        style="margin-top: 32px"
        >업로드 완료</s-button
      >
      <s-button
        v-else
        @click="onConfirmClick(0)"
        type="gray"
        style="margin-top: 32px"
        >업로드 완료</s-button
      >
      <div v-if="isUploaded" class="similar-page-box">
        <div class="d-flex align-center similar-page-section">
          나와 닮은 멍멍이들
        </div>
        <template v-if="loading">
          <div class="d-flex justify-center align-center">
            <img
              style="margin-top: 70px; width: 60vw; max-width: 300px"
              src="/static/images/loading.gif"
            />
          </div>
          <div
            style="
              margin-top: 24px;
              margin-bottom: 60px;
              font-size: 16px;
              letter-space: -0.4px;
              font-weight: 700;
              text-align: center;
              color: #585858;
            "
          >
            나와 닮은 멍멍이를 찾고있어요!<br />최대 1분의 시간이 소요될 수 있습니다.
          </div>
        </template>
        <template v-else>
          <div class="d-flex" style="flex-wrap: wrap">
            <div
              @click="onDetailClick(dog.dog_id)"
              v-for="(dog, di) in dogs"
              :key="`dog-${di}`"
              class="d-flex flex-column flex-grow-1 similar-page-item"
            >
              <div
                class="d-flex similar-page-item-image"
                :style="`background-image:url(${dog.profile})`"
              >
                <!-- <div
                v-if="Math.random() > 0.7"
                class="d-flex justify-center align-center similar-page-item-scrap"
              >
                <v-icon color="red">favorite</v-icon>
              </div> -->
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </s-main-layout>
</template>

<script>
import AWS from 'aws-sdk';
import axios from 'axios';
export default {
  name: 'my-similar-page',
  data: () => ({
    img_url: '',
    albumBucketName: 'photo-album-dog',
    bucketRegion: 'ap-northeast-2',
    IdentityPoolId: 'ap-northeast-2:caca59ba-9483-43b5-a923-f9e5c6eb3229',
    previewImage: null,
    location: '',
    dogs: [],
    isUploaded: false,
    loading: true,
  }),
  methods: {
    pickFile(e) {
      this.isUploaded = false;
      let input = this.$refs.image;
      let file = input.files;
      if (file && file[0]) {
        let reader = new FileReader();
        reader.onload = (e) => (this.previewImage = e.target.result);
        reader.readAsDataURL(file[0]);
        AWS.config.update({
          region: this.bucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: this.IdentityPoolId,
          }),
        });
        const s3 = new AWS.S3({
          apiVersion: '2006-03-01',
          params: {
            Bucket: this.albumBucketName,
          },
        });
        let photoKey = file[0].name;
        this.img_url =
          'https://photo-album-dog.s3.ap-northeast-2.amazonaws.com/' +
          encodeURIComponent(photoKey);
        // console.log(photoKey);
        s3.upload(
          {
            Key: photoKey,
            Body: file[0],
            ACL: 'public-read',
          },
          (err, data) => {
            if (err) {
              return alert(
                '사진을 업로드하는 중 오류가 발생했습니다.',
                err.message
              );
            }
            // alert('사진이 성공적으로 업로드 되었습니다.');
            // console.log(this.img_url);
          }
        );
      } else {
        this.previewImage = null;
      }
    },
    onConfirmClick(code) {
      if (code == 0) {
        alert('사진을 업로드해주세요.');
        this.isUploaded = false;
        return;
      }

      this.postMyimage();
      this.isUploaded = true;
    },
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
    async postMyimage() {
      try {
        let res = await this.$api.postMyimage({ img_url: this.img_url });
        this.dogs = res.data.data.slice(0, 9);
        this.loading = false;
      } catch (e) {
        console.error(e);
      }
    },
  },
};
</script>

<style>
.my-similar-page {
  padding: 24px 16px;
  padding-bottom: 80px;
}

.my-similar-page-image-container {
  padding-top: 24px;
  max-width: 20%;
  height: 120px;
  display: flex;
  margin: 0 auto;
}

.my-similar-page-image {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
}

.similar-page-box {
  width: 100%;
  margin-top: 32px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
  overflow: hidden;
}

.similar-page-section {
  padding: 0 16px;
  background: #fff;
  height: 40px;
  color: #ffd501;
  font-size: 16px;
  font-weight: bold;
  border-bottom: solid 1px #ffd501;
}

.similar-page-item {
  width: 33%;
}

.similar-page-item-image {
  position: relative;
  width: 100%;
  min-height: 120px;
  height: 30vw;
  max-height: 200px;
  background-size: cover;
  background-position: center center;
  border: solid 1px #fff;
}

.similar-page-item-scrap {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.61);
}
</style>