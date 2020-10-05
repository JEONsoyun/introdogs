<template>
  <s-first-layout title="멍멍이 매칭 결과">
    <div class="match-result-page">
      <s-dog-profile :data="dog" />
      <s-button @click="onDetailClick(dog.dog_id)" style="margin-top: 24px;">더 자세히 보기</s-button>
      <s-button @click="$router.push('/')" type="white" style="margin-top: 8px;">다른 멍멍이들 보러 가기</s-button>
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'match-result-page',
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
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
  }
};
</script>

<style>
.match-result-page {
    padding: 0 12px;
    padding-top: 64px;
    padding-bottom: 80px;
}
</style>