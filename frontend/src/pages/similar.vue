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
              <div
                v-if="Math.random() > 0.7"
                class="d-flex justify-center align-center similar-page-item-scrap"
              >
                <v-icon color="red">favorite</v-icon>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </s-main-layout>
</template>

<script>
import AWS from 'aws-sdk';
export default {
  name: 'my-similar-page',
  data: () => ({
    img_url: '',
    albumBucketName: 'photo-album-dog',
    bucketRegion: 'ap-northeast-2',
    IdentityPoolId: 'ap-northeast-2:caca59ba-9483-43b5-a923-f9e5c6eb3229',
    previewImage: null,
    location: '',
    dogs: [
      {
        dog_id: 'N448548202000333',
        age: '2018(년생)',
        weight: '10(Kg)',
        sex: 'W',
        kind: '진도견',
        color: '흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909319_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202009092009658.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '겁이 많고 경계심이 많아서 조심성이 많은 성격',
        find_place: '합천읍 충효로',
        find_date: '20200915',
        end_date: '20200925',
      },
      {
        dog_id: 'N442418202000563',
        age: '2017(년생)',
        weight: '4(Kg)',
        sex: 'M',
        kind: '푸들',
        color: '연갈색',
        neuter: 'U',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009141009390_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202009141009390.jpg',
        careAddr:
          '강원도 춘천시 신북읍 영서로 3282 (신북읍) (전)102보충대 주차장',
        careNm: '춘천시 동물보호센터',
        special: '온순 / 미용됨',
        find_place: '퇴계주공7차아파트 4단지부근',
        find_date: '20200914',
        end_date: '20200924',
      },
      {
        dog_id: 'N448548202000332',
        age: '2016(년생)',
        weight: '7(Kg)',
        sex: 'M',
        kind: '아메리칸 에스키모',
        color: '갈색 흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909418_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202008172108194.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '사람을 잘따르고 온순하며 밝은성격',
        find_place: '율곡면 노양3길9-1',
        find_date: '20200915',
        end_date: '20200925',
      },
      {
        dog_id: 'N442418202000563',
        age: '2017(년생)',
        weight: '4(Kg)',
        sex: 'W',
        kind: '푸들',
        color: '연갈색',
        neuter: 'U',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009141009390_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202008191508641.jpg',
        careAddr:
          '강원도 춘천시 신북읍 영서로 3282 (신북읍) (전)102보충대 주차장',
        careNm: '춘천시 동물보호센터',
        special: '온순 / 미용됨',
        find_place: '퇴계주공7차아파트 4단지부근',
        find_date: '20200914',
        end_date: '20200924',
      },
      {
        dog_id: 'N448548202000333',
        age: '2018(년생)',
        weight: '10(Kg)',
        sex: 'W',
        kind: '진도견',
        color: '흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909319_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202008221608615.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '겁이 많고 경계심이 많아서 조심성이 많은 성격',
        find_place: '합천읍 충효로',
        find_date: '20200915',
        end_date: '20200925',
      },
      {
        dog_id: 'N448548202000332',
        age: '2016(년생)',
        weight: '7(Kg)',
        sex: 'M',
        kind: '아메리칸 에스키모',
        color: '갈색 흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909418_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202008311508255.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '사람을 잘따르고 온순하며 밝은성격',
        find_place: '율곡면 노양3길9-1',
        find_date: '20200915',
        end_date: '20200925',
      },
      {
        dog_id: 'N448548202000332',
        age: '2016(년생)',
        weight: '7(Kg)',
        sex: 'M',
        kind: '아메리칸 에스키모',
        color: '갈색 흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909418_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909418.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '사람을 잘따르고 온순하며 밝은성격',
        find_place: '율곡면 노양3길9-1',
        find_date: '20200915',
        end_date: '20200925',
      },
      {
        dog_id: 'N442418202000563',
        age: '2017(년생)',
        weight: '4(Kg)',
        sex: 'W',
        kind: '푸들',
        color: '연갈색',
        neuter: 'U',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009141009390_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202009040709503.jpg',
        careAddr:
          '강원도 춘천시 신북읍 영서로 3282 (신북읍) (전)102보충대 주차장',
        careNm: '춘천시 동물보호센터',
        special: '온순 / 미용됨',
        find_place: '퇴계주공7차아파트 4단지부근',
        find_date: '20200914',
        end_date: '20200924',
      },
      {
        dog_id: 'N448548202000333',
        age: '2018(년생)',
        weight: '10(Kg)',
        sex: 'W',
        kind: '진도견',
        color: '흰색',
        neuter: 'N',
        thumnail:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909319_s.jpg',
        profile:
          'http://www.animal.go.kr/files/shelter/2020/07/202009151909319.jpg',
        careAddr:
          '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
        careNm: '태민동물병원',
        special: '겁이 많고 경계심이 많아서 조심성이 많은 성격',
        find_place: '합천읍 충효로',
        find_date: '20200915',
        end_date: '20200925',
      },
    ],
    isUploaded: false,
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
    async onConfirmClick(code) {
      if (code == 0) {
        alert('사진을 업로드해주세요.');
        this.isUploaded = false;
        return;
      }
      this.isUploaded = true;
      try {
        let d = { img_url: this.img_url };
        console.log(d);
        let res = await this.$api.postMyimage(d);
        console.log(res);
        this.dogs = res.data.data;
      } catch (e) {
        console.error(e);
      }
    },
  },
  async created() {},
};
</script>

<style>
.my-similar-page {
  padding: 24px 16px;
  padding-bottom: 40px;
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
  opacity: 0.8;
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