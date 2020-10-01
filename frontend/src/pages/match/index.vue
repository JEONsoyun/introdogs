<template>
  <s-first-layout title="나와 어울리는 멍멍이 매칭">
    <div class="match-page-container">
      <div class="match-page-box">
        <div>1. 관심이 가는 멍멍이 사진을 눌러주세요.</div>
        <div style="margin-top: 24px">
          <div class="d-flex justify-center align-center match-page-number">
            1
          </div>
          <div class="d-flex">
            <template v-for="(dog, di) in dogs">
              <div
                class="d-flex flex-column flex-grow-1 match-page-item"
                :key="`dog1-${di}`"
                v-if="di < 3"
              >
                <div
                  class="d-flex match-page-item-image"
                  :style="`background-image: url(${dog.profile})`"
                  @click="onSelectDog(0, di)"
                  :class="{
                    'match-page-item--selected': selectedDog[0] == di,
                  }"
                ></div>
              </div>
            </template>
          </div>
        </div>
        <div
          style="margin: 24px 0; width: 100%; border-bottom: solid 1px #ffd501"
        />
        <div class="d-flex justify-center align-center match-page-number">
          2
        </div>
        <div class="d-flex">
          <template v-for="(dog, dii) in dogs">
            <div
              class="d-flex flex-column flex-grow-1 match-page-item"
              :key="`dog1-${dii}`"
              v-if="dii >= 3 && dii < 6"
            >
              <div
                class="d-flex match-page-item-image"
                :style="`background-image: url(${dog.profile})`"
                @click="onSelectDog(1, dii)"
                :class="{
                  'match-page-item--selected': selectedDog[1] == dii,
                }"
              ></div>
            </div>
          </template>
        </div>
        <div
          style="margin: 24px 0; width: 100%; border-bottom: solid 1px #ffd501"
        />
        <div class="d-flex justify-center align-center match-page-number">
          3
        </div>
        <div class="d-flex">
          <template v-for="(dog, diii) in dogs">
            <div
              class="d-flex flex-column flex-grow-1 match-page-item"
              :key="`dog1-${diii}`"
              v-if="diii >= 6 && diii < 9"
            >
              <div
                class="d-flex match-page-item-image"
                :style="`background-image: url(${dog.profile})`"
                @click="onSelectDog(2, diii)"
                :class="{
                  'match-page-item--selected': selectedDog[2] == diii,
                }"
              ></div>
            </div>
          </template>
        </div>
      </div>
      <div class="match-page-box" style="margin-top: 24px">
        <div>2. 해당사항에 체크해주세요.</div>
        <v-checkbox
          v-model="pick.q1"
          color="#ffd501"
          hide-details
          label="반려견을 해외 입양하길 원하거나 한국에 거주하는 외국인인가요?"
        />
        <v-checkbox
          v-model="pick.q2"
          color="#ffd501"
          hide-details
          label="반려견으로 인한 알러지에 대해 충분하게 고려를 해보셨나요?"
        />
        <v-checkbox
          v-model="pick.q3"
          color="#ffd501"
          hide-details
          label="반려견이 혼자 있어야 하는 시간이 8시간 이상인가요?"
        />
        <v-checkbox
          v-model="pick.q4"
          color="#ffd501"
          hide-details
          label="3세 미만의 유아와 함께 살고있나요?"
        />
        <v-checkbox
          v-model="pick.q5"
          color="#ffd501"
          hide-details
          label="반려견을 기를 장소가 공장, 회사 등 사람들의 이동이 많은 곳 / 식당, 사무실 등 영업장 / 양로원 등 복지시설에 해당되나요?"
        />
        <v-checkbox
          v-model="pick.q6"
          color="#ffd501"
          hide-details
          label="반려견 입양에 대해 동거인과 합의가 되었나요?"
        />
        <v-checkbox
          v-model="pick.q7"
          color="#ffd501"
          hide-details
          label="본인이나 동거인이 우울증 등의 정신 질환이 있나요?"
        />
        <v-checkbox
          v-model="pick.q8"
          color="#ffd501"
          hide-details
          label="반려동물을 키우다가 중간에 포기한 경험이 2회 이상 있나요?"
        />
        <v-checkbox
          v-model="pick.q9"
          color="#ffd501"
          hide-details
          label="3인 이상의 가족이 실평수 10평 이하의 집에서 살고있나요?"
        />
        <div class="match-page-title">주거 형태가 어떻게 되나요?</div>
        <v-select
          class="match-page-selectbox"
          :items="type1"
          item-text="label"
          item-value="index"
          v-model="pick.q10"
          placeholder="선택해주세요"
          dense
          hide-details
          outlined
        >
          <v-col
            class="d-flex match-page-select"
            padding-top="0"
            outlined
          ></v-col>
        </v-select>
        <div class="match-page-title">
          반려견을 위해 고정적으로 지출 가능한 한달 비용은 얼마인가요?
        </div>
        <v-select
          class="match-page-selectbox"
          :items="type2"
          item-text="label"
          item-value="index"
          v-model="pick.q11"
          placeholder="선택해주세요"
          dense
          hide-details
          outlined
        >
          <v-col
            class="d-flex match-page-select"
            padding-top="0"
            outlined
          ></v-col>
        </v-select>
      </div>
      <s-button @click="onResultClick" style="margin-top: 24px"
        >결과 보기</s-button
      >
    </div>
  </s-first-layout>
</template>

<script>
export default {
  name: 'match-page',
  data: () => ({
    selectedDog: [null, null, null],
    pick: {},
    type1: [
      { index: 1, label: '다가구주택(오피스텔/아파트 등)' },
      { index: 2, label: '단독주택' },
      { index: 3, label: '기타' },
    ],
    type2: [
      { index: 1, label: '5만원 이하' },
      { index: 2, label: '5-18만원' },
      { index: 3, label: '18만원 이상' },
    ],
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
  }),
  methods: {
    onResultClick() {
      this.$router.push('/match/result');
    },
    onSelectDog(num, index) {
      this.selectedDog[num] = index;
      this.$forceUpdate();
    },
  },
};
</script>

<style>
.match-page-container {
  padding: 24px 12px;
  padding-top: 64px;
}

.match-page-box {
  width: 100%;
  padding: 16px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
}

.match-page-number {
  margin-left: 2px;
  margin-bottom: 8px;
  width: 28px;
  height: 28px;
  background: #ffd501;
  color: #fff;
  font-size: 18px;
  font-weight: bold;
  border-radius: 50%;
}

.match-page-item {
  width: 33%;
  min-height: 74px;
  height: 28vw;
  max-height: 194px;
  background: #ffd501;
  border-radius: 10px;
  overflow: hidden;
}

.match-page-item--selected {
  opacity: 0.4;
}

.match-page-item-image {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  border: solid 3px #fff;
  border-radius: 8px;
  overflow: hidden;
}

.match-page-box .v-label {
  font-size: 12px;
}

.match-page-title {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -0.39px;
  color: #616161;
  margin-bottom: 10px;
  margin-top: 25px;
  margin-left: 8px;
}

.match-page-select {
  padding-top: 0px;
}

.match-page-selectbox {
  margin-top: 0px;
  width: 100%;
  height: 44px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #1e1e1e;
}

.v-application .primary--text {
  color: #ffd501 !important;
}

.match-page-selectbox fieldset {
  border-color: #e1e1e1 !important;
  height: 48px;
  border-width: 0.1px !important;
  background: #fff;
}
</style>