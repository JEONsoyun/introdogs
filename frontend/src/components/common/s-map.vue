<template>
  <div class="d-flex s-map">
    <!-- 검색 툴바 -->

    <template v-if="!noToolbar">
      <div class="d-flex flex-grow-0 s-map-input-group">
        <input
          ref="placeNameKeyword"
          type="text"
          class="d-flex"
          style="margin-left: 8px;"
          placeholder="잃어버린 장소를 입력해주세요."
          @keydown.enter="onPlaceSearch"
        />
        <span
          class="s-map-input-group-btn d-flex flex-grow-0 flex-shrink-0 align-center justify-center"
        >
          <s-button @click="onPlaceSearch">
            <v-icon color="#fff">search</v-icon>
          </s-button>
        </span>
      </div>

      <!-- 검색 결과 -->
      <div class="s-map-searched-place-list" v-if="searchedPlaces.length > 0">
        <div
          class="d-flex align-center s-map-searched-place"
          v-for="(searchedPlace, i) of searchedPlaces"
          :key="`searchedPlace-${i}`"
          @click="onSearchedPlaceClick(searchedPlace), onPlaceSelect(searchedPlace)"
          :style="{
          background: selectedPlaceIndex == i ? '#ffd501' : null,
        }"
        >
          <div class="d-flex" :style="{
          flexGrow: 1,
        }">{{ searchedPlace.name }}</div>
          <!-- <button
            @click.stop="onPlaceSelect(searchedPlace)"
            class="d-flex flex-grow-0 flex-shrink-0 btn btn-default"
          >선택</button> -->
        </div>
      </div>

      <!-- 검색결과: 엠티뷰 -->
      <div v-if="isLoaded && searchedPlaces.length == 0" class="s-map-searched-place-list-empty">
        <template v-if="$refs.placeNameKeyword.value">검색 결과가 없습니다.</template>
        <template v-else>키워드를 입력해주세요.</template>
      </div>
    </template>

    <!-- 지도 -->
    <div :id="mapId" :style="{
      height: this.height,
    }" />
    <template v-if="!noList">
      <div class="s-map-searched-place-list" v-if="dogs.length > 0">
        <div
          class="d-flex align-center s-map-searched-place"
          v-for="(dog, index) of dogs"
          :key="`dog-${index}`"
          @click="onDogClick(dog, index)"
          :style="{
          background: selectedDogIndex == index ? '#ffd501' : null,
        }"
        >
          <div class="d-flex" :style="{
          flexGrow: 1,
        }">{{ dog.dog_id }}</div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import qs from 'querystring';

const DEFAULT_LATITUDE = 37.5690479;
const DEFAULT_LONGITUDE = 126.9749625;

/**
 * 이벤트 목록
 *
 * @cancel - 검색을 취소하고, 뒤로가기 버튼을 눌렀을 때 발생하는 이벤트
 *
 * @select - 키워드로 검색 후, 결과 선택 버튼을 클릭하였을 때 발생하는 이벤트
 * {
 *   id: <string>, // TMap 고유 장소 식별자
 *   name: <string>, // 이름
 *   latitude: <number>, // 위도
 *   longitude: <number>, // 경도
 *   data: <object>, // TMap 원본 데이터
 * }
 */
export default {
  props: {
    width: { type: String, default: '100%' },
    height: { type: String, default: '250px' },
    zoom: { type: Number, default: 14 },
    isTourApi: { type: Boolean, default: false },
    noToolbar: { type: Boolean, default: false },
    noList: { type: Boolean, default: false },
    draggable: { type: Boolean, default: true },
    dogs: { type: Array, default: () => [] },
  },
  data() {
    return {
      tData: null,
      mapId: `${Date.now()}`,
      mapObject: null,
      lastSearchTime: null,
      searchedPlaces: [],
      selectedPlaceIndex: -1,
      selectedDogIndex: 0,
      isLoaded: false,
      markers: [],
    };
  },
  watch: {
    dogs() {
      if (this.dogs.length == 0) {
        this.selectedDogIndex = -1;
        this.$emit('pickDog', {});
      } else {
        this.selectedDogIndex = 0;
        this.$emit('pickDog', this.dogs[0]);
      }
    },
  },
  methods: {
    loadResources() {
      this.tData = new Tmapv2.extension.TData();
    },
    async createMap() {
      const center = await this.getCenterPosition();
      this.mapObject = new Tmapv2.Map(this.mapId, {
        center: new Tmapv2.LatLng(center.latitude, center.longitude),
        width: this.width,
        height: this.height,
        zoom: this.zoom,
        draggable: this.draggable,
      });
      this.$emit("load");
    },
    async searchPlaces({ keyword, doSearchInKorea = false }) {
      const center = await this.getCenterPosition();
      const option = {
        page: 1,
        count: 20,
        reqCoordType: 'WGS84GEO',
        resCoordType: 'WGS84GEO',
      };

      const that = this;

      const callback = {
        onComplete: function () {
          that.onPlaceSearchComplete(this._responseData.searchPoiInfo.pois.poi);
        },
        onError: function () {
          that.onPlaceSearchError();

          if (!doSearchInKorea) {
            that.searchPlaces({ keyword, doSearchInKorea: true });
          }
        },
      };

      if (!doSearchInKorea) {
        this.tData.getPOIDataFromLonLatJson(
          center.latitude,
          center.longitude,
          encodeURIComponent(keyword),
          option,
          callback
        );
      } else {
        this.tData.getPOIDataFromSearchJson(
          encodeURIComponent(keyword),
          option,
          callback
        );
      }
    },
    /**
     * 한국 관광공사 API로 장소를 검색합니다.
     *
     * @param {string} keyword 검색할 키워드
     *
     * @returns {object} 검색결과 25개
     * {
     *   y: <number>, // 위도, latitude
     *   x: <number>, // 경도, longitude
     *   title: <string>, // 이름, string
     *   data: <object>, // 원본데이터
     * }
     */
    async searchPlacesFromTour({ keyword }) {
      const query = qs.stringify({
        ServiceKey:
          'WduuDFeO87n/Ei13xH7YO7NuR3Rc7Rlm6/iDOC6m3cBJxXjyRrZR+PzwXKsMNlWyton45LilSnz9kGXVNlhn2A==',
        MobileOS: 'ETC',
        MobileApp: 'Test',
        pageNo: 1,
        numOfRows: 25,
        keyword,
        listYN: 'Y',
        arrange: 'A',
      });

      // const res = await this.$http.get(
      //  `//api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword?${query}`
      // );
      const res = await this.$http.get(`/api/koreaTour/${keyword}`);
      const result = res.data.response.body.items.item.map((item) => ({
        y: Number(item.mapy),
        x: Number(item.mapx),
        title: item.title,
        contentId: item.contentid,
        data: item,
      }));

      this.onPlaceSearchComplete(result, true);
    },
    /**
     * 장소 식별자로 홈페이지 주소, 개요를 조회합니다.
     *
     * @param {number} contentId 장소 식별자
     *
     * @returns {object} 장소 상세정보
     * {
     *   url: <string>, // 홈페이지 주소
     *   overview: <string>, // 개요 정보
     *   data: <object>, // 원본 정보
     * }
     */
    async getPlaceDetailInfo({ contentId }) {
      const query = qs.stringify({
        ServiceKey:
          'WduuDFeO87n/Ei13xH7YO7NuR3Rc7Rlm6/iDOC6m3cBJxXjyRrZR+PzwXKsMNlWyton45LilSnz9kGXVNlhn2A==',
        MobileOS: 'ETC',
        MobileApp: 'Test',
        contentId,
        defaultYN: 'Y',
        overviewYN: 'Y',
      });

      // const res = await this.$http.get(
      //   `//api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?${query}`
      // );
      const res = await this.$http.get(`/api/koreaTourDetail/${contentId}`);
      const placeDetailInfo = res.data.response.body.items.item;
      const result = { data: placeDetailInfo };

      if (placeDetailInfo != null) {
        result.overview = placeDetailInfo.overview;

        if (placeDetailInfo.homepage != null) {
          const url = placeDetailInfo.homepage.match(
            /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/
          )[0];
          result.url = url != null ? url : null;
        } else {
          result.url = null;
        }
      } else {
        result.overview = null;
        result.url = null;
      }

      return result;
    },
    async getCenterPosition() {
      if (this.mapObject != null) {
        const center = this.mapObject.getCenter();
        return { latitude: center.lat(), longitude: center.lng() };
        // } else if (navigator.geolocation) { // 브라우저 GPS 기능 사용
        //   return await new Promise(resolve => navigator.geolocation.getCurrentPosition(pos => resolve(pos.coords)))
      } else {
        return { latitude: DEFAULT_LATITUDE, longitude: DEFAULT_LONGITUDE };
      }
    },
    onPlaceSearch() {
      const now = Date.now();

      if (this.lastSearchTime != null) {
        if (now < this.lastSearchTime + 500) {
          return;
        }
      }

      this.searchedPlaces.forEach((item) => item.marker.setMap(null));

      const keyword = this.$refs.placeNameKeyword.value;

      if (!keyword || keyword.trim().length == 0) {
        this.searchedPlaces = [];
        this.$refs.placeNameKeyword.focus();
        return;
      }

      this.lastSearchTime = now;
      if (this.isTourApi) {
        this.searchPlacesFromTour({ keyword });
      } else {
        this.searchPlaces({ keyword });
      }
    },
    onPlaceSearchComplete(searchResult, fromTourApi = false) {
      this.selectedPlaceIndex = -1;
      this.mapObject.setZoom(14);

      if (fromTourApi) {
        // 관광공사 API인 경우
        this.searchedPlaces = searchResult.map((item, index) => {
          const latitude = item.y;
          const longitude = item.x;

          item.index = index;
          item.name = `${item.title} ${
            item.data.addr1
              ? `(${item.data.addr1.split(' ').slice(0, 3).join(' ')})`
              : ''
          }`;
          item.latitude = latitude;
          item.longitude = longitude;

          const marker = new Tmapv2.Marker({
            position: new Tmapv2.LatLng(latitude, longitude),
            map: this.mapObject,
            title: item.title,
          });

          marker.addListener('click', (e) => {
            this.selectedPlaceIndex = index;
            this.mapObject.setZoom(17);
            this.mapObject.setCenter(new Tmapv2.LatLng(latitude, longitude));
          });

          return Object.assign(item, { marker });
        });
      } else {
        // TMap API인 경우
        this.searchedPlaces = searchResult.map((item, index) => {
          const [tx, ty, bx, by] = [
            Number(item.frontLat),
            Number(item.frontLon),
            Number(item.noorLat),
            Number(item.noorLon),
          ];

          const latitude = tx + (bx - bx) / 2;
          const longitude = ty + (by - ty) / 2;

          item.index = index;
          item.latitude = latitude;
          item.longitude = longitude;

          const marker = new Tmapv2.Marker({
            position: new Tmapv2.LatLng(latitude, longitude),
            map: this.mapObject,
            title: item.name,
            icon: '/static/images/location_default.png'
          });

          marker.addListener('click', (e) => {
            this.selectedPlaceIndex = index;
            this.mapObject.setZoom(17);
            this.mapObject.setCenter(new Tmapv2.LatLng(latitude, longitude));
          });

          return Object.assign(item, { marker });
        });
      }

      if (this.searchedPlaces.length > 0) {
        const firstPlace = this.searchedPlaces[0];
        this.mapObject.setCenter(
          new Tmapv2.LatLng(firstPlace.latitude, firstPlace.longitude)
        );
      }
    },
    onPlaceSearchError() {
      this.selectedPlaceIndex = -1;
      this.searchedPlaces = [];
    },
    onSearchedPlaceClick({ index, latitude, longitude }) {
      this.selectedPlaceIndex = index;
      this.mapObject.setCenter(new Tmapv2.LatLng(latitude, longitude));
      this.mapObject.setZoom(14);
    },
    async onPlaceSelect(searchedPlace) {
      this.selectedPlaceIndex = searchedPlace.index;
      let url, overview;

      // try {
      //   const res = await this.getPlaceDetailInfo({
      //     contentId: searchedPlace.contentId,
      //   });

      //   url = res.url;
      //   overview = res.overview;
      // } catch (e) {}

      const data = {
        id: searchedPlace.id,
        name: searchedPlace.name,
        latitude: searchedPlace.latitude,
        longitude: searchedPlace.longitude,
        data: searchedPlace,
      };

      // if (this.isTourApi) {
      //   Object.assign(data, {
      //     addr1: searchedPlace.data.addr1,
      //     firstimage: searchedPlace.data.firstimage,
      //     url,
      //     overview,
      //   });
      // }

      this.$emit('select', data);
    },
    onDogClick(dog, index) {
      this.selectedDogIndex = index
      this.$emit('pickDog', dog);
    },
    addMyPosition(location) {
      const { icon, latitude, longitude } = location;
      const marker = new Tmapv2.Marker({
        position: new Tmapv2.LatLng(latitude, longitude),
        map: this.mapObject,
        title: '내 위치',
        icon,
      });
    },
    addMarker(shelter) {
      const { name, latitude, longitude } = shelter;
      const marker = new Tmapv2.Marker({
        position: new Tmapv2.LatLng(latitude, longitude),
        map: this.mapObject,
        icon: '/static/images/shelter.png',
        title: name,
      });
      this.markers.push(Object.assign(marker, { shelter }));

      marker.addListener('click', (e) => {
        this.mapObject.setCenter(new Tmapv2.LatLng(latitude, longitude));
        this.$emit('pickShelter', shelter);
      });
    },
    clickMarker(index) {
      const { shelter } = this.markers[index];
      const { latitude, longitude } = shelter;
      this.mapObject.setCenter(new Tmapv2.LatLng(latitude, longitude));
      this.$emit('pickShelter', shelter);
    },
  },
  mounted() {
    this.loadResources();
    this.createMap();
    if (this.$refs.placeNameKeyword) {
      this.$refs.placeNameKeyword.focus();
    }
    this.isLoaded = true;
    if(this.noToolbar) {

    }
  },
};
</script>

<style scoped>
.s-map-input-group {
  height: 44px;
  background: #fff;
  border-bottom: solid 1px #e9e9e9;
}

.s-map-input-group-btn {
}

.s-map-input-group input {
  font-size: 14px;
  line-height: 1.29;
  letter-spacing: -0.39px;
}

.s-map-input-group input::placeholder {
  color: #c5c5c5;
}

.s-map {
  display: flex;
  flex-direction: column;
  background: #fff;
}

.s-map-searched-place-list {
  flex-grow: 1;
  min-height: 50px;
  height: 50vw;
  max-height: 160px;
  overflow-y: scroll;
}

.s-map-searched-place {
  min-height: 48px;
  display: flex;
  padding: 0 12px;
  font-size: 14px;
  letter-spacing: -0.48px;
  color: #585858;
  font-weight: 700;
}

.s-map-searched-place:not(:last-child) {
  box-shadow: 0 1px 0 0 #e8e8e8;
}

.s-map-searched-place-list-empty {
  min-height: 50px;
  height: 50vw;
  max-height: 160px;
  display: flex;
  flex-shrink: 1;
  flex-grow: 1;
  align-items: center;
  justify-content: center;
  color: #888;
}
</style>
