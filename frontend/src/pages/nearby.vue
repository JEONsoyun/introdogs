<template>
  <s-main-layout title="내 주변 멍멍이 찾기">
    <div class="nearby-page">
      <div class="nearby-page-map">
        <s-map noToolbar />
      </div>
      <s-dog-profile-small
        style="margin-top:-1px;border-top-right-radius:0;border-top-left-radius:0;"
        :data="dog"
      />
      <s-button
        @click="onDetailClick"
        style="border-top-left-radius:0;border-top-right-radius:0;"
        size="small"
      >자세히 보기</s-button>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'nearby-page',
  data: () => ({
    dog: {
      dog_id: 'N448548202000333',
      age: '2020(년생)',
      weight: '1(Kg)',
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
  }),
  methods: {
    onDetailClick() {
      this.$router.push(`/detail/${this.dog.dog_id}`);
    },
  },
};
</script>

<style>
.nearby-page {
  padding: 24px 16px;
  padding-bottom: 80px;
}

.nearby-page-map {
  border-top-right-radius: 4px;
  border-top-left-radius: 4px;
  overflow: hidden;
  border: solid 1px #ffd501;
}
</style>