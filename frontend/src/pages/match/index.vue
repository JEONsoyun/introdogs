<template>
  <s-first-layout title="나와 어울리는 멍멍이 매칭">
    <div class="match-page-container">
      <div class="match-page-box">
        <div>1. 관심있는 멍멍이 사진을 선택해주세요.</div>
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
                  @click="onSelectDog(0, di + 1)"
                  :class="{
                    'match-page-item--selected': pick.p1 == di + 1,
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
                @click="onSelectDog(1, (dii % 3) + 1)"
                :class="{
                  'match-page-item--selected': pick.p2 == (dii % 3) + 1,
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
                @click="onSelectDog(2, (diii % 3) + 1)"
                :class="{
                  'match-page-item--selected': pick.p3 == (diii % 3) + 1,
                }"
              ></div>
            </div>
          </template>
        </div>
      </div>
      <div class="match-page-box" style="margin-top: 24px">
        <div>2. 해당사항에 체크해주세요.</div>
        <v-checkbox
          v-model="survey.q1"
          color="#ffd501"
          hide-details
          label="반려견을 해외 입양하길 원하거나 한국에 거주하는 외국인인가요?"
        />
        <v-checkbox
          v-model="survey.q2"
          color="#ffd501"
          hide-details
          label="반려견으로 인한 알러지에 대해 충분하게 고려를 해보셨나요?"
        />
        <v-checkbox
          v-model="survey.q3"
          color="#ffd501"
          hide-details
          label="반려견이 혼자 있어야 하는 시간이 8시간 이상인가요?"
        />
        <v-checkbox
          v-model="survey.q4"
          color="#ffd501"
          hide-details
          label="3세 미만의 유아와 함께 살고있나요?"
        />
        <v-checkbox
          v-model="survey.q5"
          color="#ffd501"
          hide-details
          label="반려견을 기를 장소가 공장, 회사 등 사람들의 이동이 많은 곳 / 식당, 사무실 등 영업장 / 양로원 등 복지시설에 해당되나요?"
        />
        <v-checkbox
          v-model="survey.q6"
          color="#ffd501"
          hide-details
          label="반려견 입양에 대해 동거인과 합의가 되었나요?"
        />
        <v-checkbox
          v-model="survey.q7"
          color="#ffd501"
          hide-details
          label="본인이나 동거인이 우울증 등의 정신 질환이 있나요?"
        />
        <v-checkbox
          v-model="survey.q8"
          color="#ffd501"
          hide-details
          label="반려동물을 키우다가 중간에 포기한 경험이 2회 이상 있나요?"
        />
        <v-checkbox
          v-model="survey.q9"
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
          v-model="survey.q10"
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
          v-model="survey.q11"
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
    pick: {},
    survey: {
      q1: false,
      q2: false,
      q3: false,
      q4: false,
      q5: false,
      q6: false,
      q7: false,
      q8: false,
      q9: false,
    },
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
        kind: '말티즈',
        profile: '/static/images/dog_m.PNG',
      },
      {
        kind: '진도견',
        profile: '/static/images/dog_j.PNG',
      },
      {
        kind: '포메',
        profile: '/static/images/dog_pm.PNG',
      },
      {
        kind: '푸들',
        profile: '/static/images/dog_pd.PNG',
      },
      {
        kind: '치와와',
        profile: '/static/images/dog_c.PNG',
      },
      {
        kind: '닥스훈트',
        profile: '/static/images/dog_d.PNG',
      },
      {
        kind: '요크셔테리어',
        profile: '/static/images/dog_y.PNG',
      },
      {
        kind: '리트리버',
        profile: '/static/images/dog_r.PNG',
      },
      {
        kind: '시츄',
        profile: '/static/images/dog_s.PNG',
      },
    ],
  }),
  methods: {
    onResultClick() {
      if (
        this.pick.p1 == null ||
        this.pick.p2 == null ||
        this.pick.p3 == null
      ) {
        alert('관심있는 멍멍이 사진을 선택해주세요.');
      } else if (!this.survey.q10) {
        alert('주거 형태를 선택해주세요.');
      } else if (!this.survey.q11) {
        alert('가능한 고정 지출 비용을 선택해주세요.');
      }

      if (this.survey.q5 == false) {
        this.survey.q5 = 4;
      } else {
        this.survey.q5 = 1;
      }

      this.$router.push({
        path: '/match/result',
        query: {
          pick: Object.assign(this.pick),
          survey: Object.assign(this.survey),
        },
      });
    },
    onSelectDog(num, index) {
      if (num == 0) {
        this.pick.p1 = index;
      } else if (num == 1) {
        this.pick.p2 = index;
      } else {
        this.pick.p3 = index;
      }
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