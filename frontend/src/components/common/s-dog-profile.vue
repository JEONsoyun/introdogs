<template>
  <div class="s-dog-profile-box">
    <template v-if="isDetail">
      <div
        class="d-flex align-center s-dog-profile-section"
        style="margin-top: -16px"
      >
        멍멍이 정보
      </div>
    </template>
    <div
      class="s-dog-profile-image"
      :style="`background-image: url(${data.profile ? data.profile : '/static/images/empty_dog.png'})`"
    />
    <div class="s-dog-profile-content">
      <div style="padding: 0 16px">{{ data.dog_id }}</div>
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">나이</div>
          <div class="s-dog-profile-text">{{ data.age }}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">성별</div>
          <div class="s-dog-profile-text">
            {{ data.sex == 'M' ? '남' : '여' }}
          </div>
        </div>
      </div>
      <div class="s-dog-profile-bar" />
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">견종</div>
          <div class="s-dog-profile-text">{{ data.kind }}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">털색</div>
          <div class="s-dog-profile-text">{{ data.color }}</div>
        </div>
      </div>

      <div class="s-dog-profile-bar" />
      <div class="d-flex">
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">무게</div>
          <div class="s-dog-profile-text">{{ data.weight }}</div>
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">중성화 여부</div>
          <div class="s-dog-profile-text">{{ data.neuter }}</div>
        </div>
      </div>
      <div class="s-dog-profile-bar" />
      <div class="d-flex s-dog-profile-row">
        <div class="s-dog-profile-title">특징</div>
        <div class="s-dog-profile-text">{{ data.special }}</div>
      </div>
      <template v-if="isDetail">
        <div
          class="d-flex align-center s-dog-profile-section"
          style="margin-top: 16px; margin-bottom: 0"
        >
          보호소 정보
        </div>
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">보호소</div>
          <div class="s-dog-profile-text">{{ data.shelter_name }}</div>
        </div>
        <div class="s-dog-profile-bar" />
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">발견 장소</div>
          <div class="s-dog-profile-text">{{ data.find_place }}</div>
        </div>
        <div class="s-dog-profile-bar" />
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">발견 날짜</div>
          <div class="s-dog-profile-text">{{ data.find_date }}</div>
        </div>
        <div class="s-dog-profile-bar" />
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">보호 기간</div>
          <div class="s-dog-profile-text">
            {{ data.find_date }} ~ {{ data.end_date }}
          </div>
        </div>
        <div class="s-dog-profile-bar" />
        <div class="d-flex s-dog-profile-row">
          <div class="s-dog-profile-title">보호소 주소</div>
          <div class="s-dog-profile-text">{{ data.careAddr }}</div>
        </div>
        <div class="s-dog-proflie-map">
          <s-map
            v-if="data.shelter && data.shelter.length != 0"
            height="200px"
            ref="map"
            :zoom="16"
            @load="onMapLoad"
            noToolbar
            noList
          />
        </div>
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 's-dog-profile',
  props: {
    data: { type: Object, default: () => ({}) },
    isDetail: { type: Boolean, default: false },
  },
  data: () => ({}),
  methods: {
    onMapLoad() {
      console.log(this.data);
      this.$refs.map.addMyPosition({
        icon: '/static/images/location.png',
        latitude: this.data.shelter
          ? this.data.shelter[0].shelter_lat
          : 37.8701158122,
        longitude: this.data.shelter
          ? this.data.shelter[0].shelter_lng
          : 126.9835430508,
      });
      this.$refs.map.mapObject.setCenter(
        new Tmapv2.LatLng(
          this.data.shelter
            ? Number(this.data.shelter[0].shelter_lat)
            : 37.8701158122,
          this.data.shelter
            ? Number(this.data.shelter[0].shelter_lng)
            : 126.9835430508
        )
      );
    },
  },
};
</script>

<style>
.s-dog-profile-box {
  width: 100%;
  padding-top: 16px;
  border-radius: 4px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.48px;
  color: #1e1e1e;
  overflow: hidden;
}

.s-dog-profile-section {
  padding: 0 16px;
  margin-bottom: 16px;
  background: #ffd501;
  height: 30px;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
}

.s-dog-profile-image {
  margin: 0 16px 16px 16px;
  min-height: 214px;
  height: 40vh;
  max-height: 500px;
  background-size: cover;
  background-position: center center;
}

.s-dog-profile-row {
  width: 100%;
  padding: 12px 16px;
  min-height: 42px;
  display: flex;
  align-items: center;
}

.s-dog-profile-title {
  color: #ffd501;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -0.6px;
  margin-right: 10px;
  flex-shrink: 0;
}

.s-dog-profile-text {
  font-size: 12px;
  font-weight: 400;
  letter-spacing: -0.48px;
  color: #616161;
}

.s-dog-profile-bar {
  width: 100%;
  border-bottom: solid 1px #eee;
}

.s-dog-proflie-map {
  width: 100%;
}
</style>