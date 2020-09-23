<template>
  <s-main-layout title="나와 닮은 멍멍이">
    <div class="similar">
      <template v-if="dog != null && dog.id != null">
        <s-dog-profile :data="dog" />
        <s-button style="margin-top: 24px;">다시 찾아보기</s-button>
      </template>
      <template v-else>
          <div class="d-flex flex-column justify-center align-center ">
          <img class="similar-empty-image" src="/static/images/question_dog.png"/>
          <div class="similar-empty-text">나와 닮은 멍멍이 기록이 없네요!</div>
          </div>
          <s-button style="margin-top: 24px;">나와 닮은 멍멍이 찾으러 가기</s-button>
      </template>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'similar',
  data: () => ({
    dog: {
    //   dog_id: 'N448548202000333',
    //   age: '2018(년생)',
    //   weight: '10(Kg)',
    //   sex: 'M',
    //   kind: '진도견',
    //   color: '흰색',
    //   neuter: 'N',
    //   thumnail:
    //     'http://www.animal.go.kr/files/shelter/2020/07/202009151909319_s.jpg',
    //   profile:
    //     'http://www.animal.go.kr/files/shelter/2020/07/202009151909319.jpg',
    //   careAddr:
    //     '경상남도 합천군 합천읍 옥산로 16 (합천읍/ 까치빌라) 태민동물병원',
    //   careNm: '태민동물병원',
    //   special: '겁이 많고 경계심이 많아서 조심성이 많은 성격',
    //   find_place: '합천읍 충효로',
    //   find_date: '20200915',
    //   end_date: '20200925',
    },
  }),
};
</script>

<style>
.similar {
  padding: 24px 12px;
}

.similar-empty-image {
    margin-top: 24px;
    width: 220px;
    opacity: 0.4;
}

.similar-empty-text {
    margin: 32px;
    font-size: 16px;
    color: #585858;
}
</style>