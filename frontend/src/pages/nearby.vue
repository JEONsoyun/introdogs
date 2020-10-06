<template>
  <s-main-layout title="내 주변 멍멍이 찾기">
    <div class="nearby-page">
      <div class="nearby-page-map">
        <s-map
          @load="onMapLoad"
          @pickDog="onPickDog"
          @pickShelter="onPickShelter"
          ref="map"
          :zoom="10"
          noToolbar
          :dogs="dogs"
        />
      </div>
      <div v-if="selectedShelter" class="nearby-page-shelter">
        {{ selectedShelter }}
      </div>
      <template v-if="dog.dog_id != null">
        <s-dog-profile-small
          style="
            margin-top: -1px;
            border-top-right-radius: 0;
            border-top-left-radius: 0;
          "
          :data="dog"
        />
        <s-button
          @click="onDetailClick(dog.dog_id)"
          style="border-top-left-radius: 0; border-top-right-radius: 0"
          size="small"
          >자세히 보기</s-button
        >
      </template>
      <template
        v-if="shelters.length != 0 && shelters != null && dog.dog_id == null"
      >
        <div class="d-flex flex-column justify-center align-center">
          <img
            class="nearby-page-empty-image"
            src="/static/images/question_dog.png"
            style="margin-top: 24px"
          />
          <div class="nearby-page-empty-text">
            {{ selectedShelter }}에 정보가 없습니다.<br />
            다른 보호소를 선택해주세요.
          </div>
        </div>
      </template>
      <template v-if="shelters.length == 0 || shelters == null">
        <div class="d-flex flex-column justify-center align-center">
          <img
            class="nearby-page-empty-image"
            src="/static/images/question_house.png"
          />
          <div class="nearby-page-empty-text">
            주변에 보호소 정보가 없습니다.
          </div>
        </div>
      </template>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'nearby-page',
  data: () => ({
    dogs: [],
    dog: {},
    shelters: [],
    clatitude: null,
    clongitude: null,
    selectedShelter: '',
  }),
  methods: {
    onDetailClick(id) {
      this.$router.push(`/detail/${id}`);
    },
    onMapLoad() {
      console.log(this.clatitude);
      if (this.clatitude) {
        this.updateMapCenter();
        this.initshelters();
        this.$refs.map.addMyPosition({
          icon: '/static/images/location.png',
          latitude: this.clatitude ? this.clatitude : 37.8701158122,
          longitude: this.clongitude ? this.clongitude : 126.9835430508,
        });
      }
    },
    updateMapCenter() {
      let latLng = new Tmapv2.LatLng(
        Number(this.clatitude) || 0,
        Number(this.clongitude) || 0
      );

      this.$refs.map.mapObject.setCenter(latLng);
    },
    async onPickShelter(shelter) {
      this.selectedShelter = shelter.name;
      try {
        let res = await this.$api.getArroundDogs(shelter.name);
        console.log(res);
        this.dogs = res.dogs;
      } catch (e) {
        console.error(e);
      }
    },
    async initshelters() {
      try {
        let res = await this.$api.getShelters({
          shelter_lat: this.clatitude,
          shelter_lng: this.clongitude,
        });
        this.shelters = res.data;
        console.log(this.shelters);
        this.shelters.forEach(({ shelter_name, shelter_lat, shelter_lng }) => {
          this.$refs.map.addMarker({
            name: shelter_name,
            latitude: shelter_lat,
            longitude: shelter_lng,
          });
        });

        if (this.shelters.length > 0) {
          this.$refs.map.clickMarker(0);
        }
      } catch (e) {
        console.error(e);
      }
    },
    onPickDog(dog) {
      this.dog = dog;
    },
    getCurrentPositionSuccess(pos) {
      console.log(pos);
      this.clatitude = pos.coords.latitude;
      this.clongitude = pos.coords.longitude;
      this.onMapLoad();
      this.$forceUpdate();
    },
  },
  created() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(this.getCurrentPositionSuccess);
    }
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

.nearby-page-shelter {
  background: #ffd501;
  padding: 4px 16px;
  color: #fff;
  font-weight: 800;
}

.nearby-page-empty-image {
  margin-top: 32px;
  width: 120px;
  opacity: 0.4;
}

.nearby-page-empty-text {
  margin: 32px;
  font-size: 16px;
  color: #585858;
  text-align: center;
}
</style>