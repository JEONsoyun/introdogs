<template>
  <s-main-layout title="멍멍이 상세보기">
    <div class="detail-page">
      <div class="d-flex align-center" style="margin-bottom: 8px;">
        <div class="detail-page-title">{{dog.dog_id}}</div>
        <div class="d-flex" />
        <div @click="onScrapClick">
          <v-icon v-if="isScrapped" size="36" color="red">favorite</v-icon>
          <v-icon v-if="!isScrapped" size="36" color="red">favorite_border</v-icon>
        </div>
      </div>
      <s-dog-profile :data="dog" isDetail />
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'detail-page',
  data: () => ({
    dogId: 0,
    dog: {
      dog_id: 'N448548202000333',
      age: '2018(년생)',
      weight: '10(Kg)',
      sex: 'M',
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
    isScrapped: false,
  }),
  methods: {
    onScrapClick() {
      this.isScrapped = !this.isScrapped
    }
  },
  created() {
    this.dogId = this.$route.params.id;
    // dog api 부르기
  },
};
</script>

<style>
.detail-page {
  padding: 24px 16px;
  padding-bottom: 80px;
}

.detail-page-title {
  font-size: 16px;
  letter-spacing: -0.48px;
  font-weight: bold;
}
</style>