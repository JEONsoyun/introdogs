<template>
  <s-first-layout title="잃어버린 멍멍이 찾기">
    <div class="lost-page">
      <div @click.stop="$refs.image.click">
        <s-button>
          <v-icon color="#fff">photo_camera</v-icon>
          <div style="margin-left: 4px">멍멍이 사진 업로드</div>
        </s-button>
        <input
          accept="image/*"
          class="d-none"
          ref="image"
          type="file"
          @input="pickFile"
        />
      </div>
      <div class="d-flex justify-center lost-page-image-container">
        <div
          class="lost-page-image"
          v-if="previewImage"
          :style="`background-image:url(${previewImage})`"
        />
      </div>
      <div class="lost-page-map" style="margin-top: 32px">
        <s-map noList />
      </div>
      <s-button @click="onConfirmClick" style="margin-top: 32px"
        >입력 완료</s-button
      >
    </div>
  </s-first-layout>
</template>

<script>
import AWS from 'aws-sdk';
import axios from 'axios';
export default {
  name: 'lost-page',
  data: () => ({
    previewImage: null,
    location: '',
    img_url: '',
    albumBucketName: 'photo-album-dog',
    bucketRegion: 'ap-northeast-2',
    IdentityPoolId: 'ap-northeast-2:caca59ba-9483-43b5-a923-f9e5c6eb3229',
  }),
  methods: {
    pickFile(e) {
      let input = this.$refs.image;
      let file = input.files;
      console.dir(file[0]);
      if (file && file[0]) {
        //console.log('if로그 ');
        // console.log(file[0]);
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
        console.log(photoKey);
        s3.upload(
          {
            Key: photoKey,
            Body: file[0],
            ACL: 'public-read',
          },
          (err, data) => {
            if (err) {
              return alert(
                'There was an error uploading your photo: ',
                err.message
              );
            }
            alert('Successfully uploaded photo.');
            console.log(this.img_url);
          }
        );
      } else {
        this.previewImage = null;
      }
    },
    onConfirmClick() {
      axios({
        method: 'post',
        url: 'http://j3a307.p.ssafy.io:8000/losts/',
        data: {
          img_url: this.img_url,
          shelter_lat: '37.544846922',
          shelter_lng: '126.939479132',
        },
      }).then((res) => {
        this.$router.push('/lost/result');
      });
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
  border-radius: 4px;
  overflow: hidden;
  border: solid 1px #ffd501;
}
</style>