<template>
  <s-first-layout title="잃어버린 멍멍이 찾기 결과">
    <div class="lost-result-page">
      <div class="lost-result-page-map">
      <s-map />
      </div>
      <s-dog-profile-small style="margin-top: 24px;" :data="dog" />
      <s-button
        @click="onDetailClick"
        style="border-top-left-radius:0;border-top-right-radius:0;"
        size="small"
      >자세히 보기</s-button>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'lost-result-page',
  data: () => ({
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
  }),
  methods: {
    onDetailClick() {
      this.$router.push(`/detail/${this.dog.dog_id}`);
    },
  },
};
</script>

<style>
.lost-result-page {
  padding: 0 16px;
  padding-top: 64px;
  padding-bottom: 80px;
}

.lost-result-page-map {
  border-radius: 4px;
  overflow: hidden;
  border: solid 1px #ffd501;
}

</style>