<template>
  <s-main-layout>
    <div class="index-filter-container">filter area</div>
    <div class="index-item-container">
      <div class="d-flex" style="flex-wrap: wrap;">
        <div v-for="(dog, di) in dogs" class="d-flex" :key="`dog-${di}`">
          <div class="d-flex flex-column index-item">
            <div class="index-item-image" :style="`background-image:url(${dog.thumnail})`"/>
            <div class="index-item-content">
              <div>{{dog.dog_id}}</div>
              <div>{{dog.age}}</div>
              <div>{{dog.sex}}</div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'index',
  data: () => ({
    dogs: [
      {
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
    ],
  }),
  methods: {
    // async getBest(cnt) {
    //   try {
    //     if (cnt != 0) {
    //       this.cnt += cnt;
    //     }
    //     let temp = await this.$api.getBest(this.startNum, this.cnt);
    //     this.best = temp;
    //     for (let i = 0; i < this.best.length; i++) {}
    //   } catch (e) {
    //     console.error(e);
    //   }
    // }
  },
  async created() {
    // this.getBest(0);
    for (var i = 0; i < 10; ++i) {
      this.dogs.push(this.dogs[0]);
      this.dogs.push(this.dogs[1]);
      this.dogs.push(this.dogs[2]);
    }
  },
};
</script>

<style>
.index-filter-container {
  height: 120px;
}
.index-item-container {
  width: 100%;
}

.index-item {
  width: 33vw;
  background: #eee;
}

.index-item-image {
  width: 33vw;
  height: 33vw;
  background-size: cover;
  background-position: center center;
  opacity: 0.8;
}

.index-item-content {
  width: 100%;
  height: 40px;
  font-size: 10px;
}
</style>

