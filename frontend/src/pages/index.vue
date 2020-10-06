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
            >
              <div
                @click="onColorClick(ci)"
                :style="`width:100%;height:100%;border-radius:50%;background: ${color.code}`"
                :class="{
                  'main-page-filter-color--selected': selectedColor[ci],
                }"
              ></div>
            </div>
          </div>
          <div class="d-flex align-center" style="margin-bottom: 8px">
            <div
              class="d-flex flex-grow-0 main-page-filter-gender"
              style="background-image: url('/static/images/male.png')"
              @click="onGenderClick(0)"
            >
              <div
                :class="{
                  'main-page-filter-gender--selected': selectedGender[0],
                }"
              ></div>
            </div>
            <div
              class="d-flex flex-grow-0 main-page-filter-gender"
              style="background-image: url('/static/images/female.png')"
              @click="onGenderClick(1)"
            >
              <div
                :class="{
                  'main-page-filter-gender--selected': selectedGender[1],
                }"
              ></div>
            </div>
            <div class="d-flex" />
            <div class="d-flex flex-grow-0">
              <s-button @click="onFilterChange" size="small">확인</s-button>
            </div>
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <div class="main-page-item-container">
      <template v-if="loading">
        <div class="d-flex justify-center align-center">
          <img
            style="margin-top: 70px; width: 60vw; max-width: 300px"
            src="/static/images/loading.gif"
          />
        </div>
        <div
          style="
            margin: 24px 0;
            font-size: 16px;
            letter-space: -0.4px;
            font-weight: 700;
            text-align: center;
            color: #585858;
          "
        >
          멍멍이들을 데려오는 중입니다!<br />잠시만 기다려주세요.
        </div>
      </template>
      <template v-else>
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
                <!-- <div
                  v-if="scraps.length != 0 && scraps != null && scraps[di]"
                  class="d-flex justify-center align-center main-page-item-scrap"
                >
                  <v-icon color="red">favorite</v-icon>
                </div> -->
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
        </div>
      </template>
      <div
        v-if="!loading && dogs.length != 0 && dogs != null"
        @click="onMoreClick"
        class="d-flex align-center justify-center main-page-more"
      >
        더 보기
        <v-icon color="#616161">expand_more</v-icon>
      </div>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'main-page',
  data: () => ({
    loading: true,
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
      pick: {},
      survey: {},
      color: [],
      sex: 'X',
    },
    dogs: [],
    scrapDogs: [],
    isFilterVisible: false,
    scraps: [],
    selectedColor: [],
    selectedGender: [],
  }),
  methods: {
    async getDogs() {
      let q = this.$route.query;
      for (let i in q.color) {
        this.data.color.push(this.colors[q.color[i]].tag);
      }

      if (!q.gender || q.gender.length != 1) {
        this.data.sex = 'X';
      } else {
        if (q.gender[0] == 0) {
          this.data.sex = 'M';
        } else {
          this.data.sex = 'F';
        }
      }
      try {
        let res = await this.$api.getDogs(this.data);
        this.dogs = res.data;
        this.loading = false;
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
    onMoreClick() {
      alert('더 불러올 데이터가 없습니다.');
    },
    async getScraps() {
      try {
        let res = await this.$api.getScraps();
        if (!res.user) {
          return;
        }
        this.scrapDogs = res.user[0].dog_info;
      } catch (e) {
        console.error(e);
      }
    },
    onColorClick(index) {
      this.selectedColor[index] = !this.selectedColor[index];
      this.$forceUpdate();
    },
    onGenderClick(index) {
      this.selectedGender[index] = !this.selectedGender[index];
      this.$forceUpdate();
    },
    onFilterChange() {
      let selectedColors = [];
      for (let i in this.selectedColor) {
        if (this.selectedColor[i]) {
          selectedColors.push(i);
        }
      }
      let selectedGenders = [];
      for (let i in this.selectedGender) {
        if (this.selectedGender[i]) {
          selectedGenders.push(i);
        }
      }
      this.$router.push({
        path: '/filter',
        query: { color: selectedColors, gender: selectedGenders },
      });

      this.getDogs();
    },
  },
  async created() {
    // let q = this.$route.query;
    // for (let color in q.color) {
    //   for (let j in this.colors) {
    //     if (color == this.colors[j].key) {
    //       this.selectedColor[j] = true;
    //       return;
    //     }
    //   }
    // }
    // console.log("***", this.selectedColor);
    // this.$forceUpdate();
    // await this.getScraps();
    await this.getDogs();
    for (let i in this.dogs) {
      for (let j in this.scrapDogs) {
        if (this.scrapDogs[j].dog_id == this.dogs[i].dog_id) {
          this.scraps[i] = true;
        }
      }
    }
    this.$forceUpdate();
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
  background: #ffd501;
  border: solid 2px #ffd501;
  overflow: hidden;
}

.main-page-filter-color--selected {
  opacity: 0.3;
}

.main-page-filter-gender {
  margin-right: 2px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: solid 2px #ffd501;
  background-size: cover;
  background-position: center center;
  overflow: hidden;
}

.main-page-filter-gender--selected {
  width: 100%;
  height: 100%;
  background: #ffd501;
  opacity: 0.7;
  border-radius: 50%;
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

