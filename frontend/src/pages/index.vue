<template>
  <s-main-layout>
    <v-expansion-panels class="main-page-filter-container">
      <v-expansion-panel>
        <v-expansion-panel-header>
          <div class="d-flex" />
          <v-icon class="d-flex flex-grow-0" size="14px">pets</v-icon>
          <div
            class="d-flex flex-grow-0"
            style="
              margin-left: 4px;
              color: rgba(0, 0, 0, 0.54);
              font-weight: bold;
              font-size: 12px;
              margin-right: 4px;
            "
          >
            멍멍이 스타일
          </div>
          <template v-slot:actions>
            <v-icon>expand_more</v-icon>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <div
            class="d-flex align-center"
            style="flex-wrap: wrap; margin-bottom: 12px"
          >
            <div
              v-for="(color, ci) in colors"
              :key="`color-${ci}`"
              class="d-flex flex-grow-0 flex-shrink-0 main-page-filter-color"
              :style="`background: ${color.code}`"
            ></div>
          </div>
          <div class="d-flex align-center" style="margin-bottom: 8px">
            <img
              class="d-flex flex-grow-0 main-page-filter-gender"
              src="/static/images/male.png"
            />
            <img
              class="d-flex flex-grow-0 main-page-filter-gender"
              src="/static/images/female.png"
            />
            <div class="d-flex" />
            <div class="d-flex flex-grow-0">
              <s-button size="small">확인</s-button>
            </div>
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <div class="main-page-item-container">
      <div class="d-flex" style="flex-wrap: wrap">
        <div
          @click="onDetailClick(dog.dog_id)"
          v-for="(dog, di) in dogs"
          class="d-flex main-page-item"
          :key="`dog-${di}`"
        >
          <div class="d-flex flex-column flex-grow-1">
            <div
              class="d-flex flex-shrink-1 main-page-item-image"
              :style="`background-image:url(${dog.profile})`"
            >
              <div
                v-if="Math.random() > 0.7"
                class="d-flex justify-center align-center main-page-item-scrap"
              >
                <v-icon color="red">favorite</v-icon>
              </div>
            </div>
            <div class="main-page-item-content">
              <div class="main-page-item-id-container">
                <div class="main-page-item-id">{{ dog.dog_id }}</div>
              </div>
              <div class="d-flex align-center">
                <div>{{ dog.age }}</div>
                <div class="d-flex" />
                <img
                  v-if="dog.sex == 'M'"
                  src="/static/images/male.png"
                  style="width: 25px; height: 25px"
                />
                <img
                  v-else
                  src="/static/images/female.png"
                  style="width: 25px; height: 25px"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="d-flex align-center justify-center main-page-more">
          더 보기
          <v-icon color="#616161">expand_more</v-icon>
        </div>
      </div>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'main-page',
  data: () => ({
    colors: {
      white: { tag: ['흰', '하양', '백'], code: '#fff' },
      cream: { tag: ['크림', '아이보리', '미'], code: 'rgb(255, 249, 223)' },
      beige: {
        tag: ['베이지', '황백', '살구', '연갈'],
        code: 'rgb(197, 181, 146)',
      },
      yellow: {
        tag: ['황', '노', '주황', '금', '골드', '누렁'],
        code: 'rgb(163, 120, 26)',
      },
      brown: {
        tag: ['갈', '초코', '고동', '밤', '레드'],
        code: 'rgb(59, 28, 3)',
      },
      black: { tag: ['검', '블랙', '흑', '탄'], code: '#000' },
      gray: { tag: ['회', '실버', '잿빛'], code: 'rgb(68, 68, 68)' },
      spotted: {
        tag: ['얼룩', '점박이', '호피', ' 바둑'],
        code:
          'linear-gradient(rgb(255, 255, 255),rgb(138, 85, 49),rgb(0, 0, 0))',
      },
    },
    data: {
      color: [],
      sex: 'X',
    },
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
    isFilterVisible: false,
  }),
  methods: {
    async getDogs() {
      try {
        let res = await this.$api.getDogs(this.data);
        this.dogs = res;
      } catch (e) {
        console.error(e);
      }
    },
    onFilterClick() {
      this.isFilterVisible = !this.isFilterVisible;
    },
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
  },
  async created() {
    // this.getDogs();
    for (let i = 0; i < 9; ++i) {
      this.dogs.push(this.dogs[i]);
    }
  },
  mounted() {
    if (this.$store.state.ISSKIP) {
      return;
    }
    if (!localStorage.getItem('isChecked')) {
      this.$router.push('/first');
    }
  },
};
</script>

<style>
.main-page-filter-container {
  position: fixed !important;
  top: 48px !important;
  left: 0 !important;
  width: 100% !important;
  z-index: 2 !important;
  background: #fbfbfb !important;
  border-radius: 0 !important;
}

.main-page-filter-color {
  margin-right: 2px;
  margin-bottom: 2px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: solid 2px #ffd501;
}

.main-page-filter-gender {
  margin-right: 2px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: solid 2px #ffd501;
}

.main-page-item-container {
  width: 100%;
  padding-top: 48px;
}

.main-page-item {
  width: 33%;
  border-left: solid 1px #fff;
  border-top: solid 1px #fff;
}

.main-page-item:nth-child(1) {
  border: 0;
}

.main-page-item:nth-child(2),
.main-page-item:nth-child(3) {
  border-top: 0;
}

.main-page-item:nth-child(3n + 1) {
  border-left: 0;
}

.main-page-item-id-container {
  position: relative;
  height: 16px;
  overflow: hidden;
}

.main-page-item-id {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  text-overflow: ellipsis;
  overflow: hidden;
}

.main-page-item-image {
  position: relative;
  width: 100%;
  min-height: 100px;
  height: 30vw;
  max-height: 200px;
  background-size: cover;
  background-position: center center;
}

.main-page-item-scrap {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.61);
}

.main-page-item-content {
  padding: 4px;
  width: 100%;
  font-size: 10px;
  font-weight: bold;
  background: #fff9dc;
}

.main-page-more {
  font-size: 14px;
  font-weight: bold;
  height: 70px;
  color: #616161;
  padding-bottom: 8px;
}
</style>

