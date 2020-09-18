<template>
  <s-main-layout title="프로필" noArrow>
    <div class="d-flex flex-column">
      <div class="login-top">
        <div class="login-text1">로그인이 필요합니다</div>
        <div class="login-text2">나와 잘 맞는 멍멍이 추천 시스템을 경험해보세요!</div>
      </div>
      <div class="login-content">
        <div class="login-container">
          <div class="login-id">
            <v-text-field
              label="이메일 입력"
              v-model="data.memberEmail"
              single-line
              solo
              flat
              height="44px"
              hide-details
            ></v-text-field>
          </div>
          <div class="login-pwd">
            <v-text-field
              label="비밀번호 입력"
              v-model="data.memberPw"
              single-line
              solo
              flat
              height="44px"
              type="password"
              class="login-password"
              hide-details
            ></v-text-field>
          </div>
        </div>
        <div class="login-btns">
          <div @click="onLoginClick" class="login-button">로그인</div>
          <div class="login-create" @click="onSignupClick">회원가입</div>
        </div>
        <!-- SYJ 1차 배포 주석 
        <div class="login-find">
          <div class="login-findid" onclick="location.href='findId'">아이디 찾기</div>
          <div class="login-findline"></div>
          <div class="login-findpwd" onclick="location.href='findPw'">비밀번호 찾기</div>
        </div>
        -->
      </div>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'login',
  data: () => ({
    data: {},
  }),
  methods: {
    async onLoginClick() {
      try {
        await this.$api.login(this.data);
        location.href = '/tour';
      } catch (e) {
        alert('아이디 또는 비밀번호를 확인해주세요.');
      }
    },
    onSignupClick() {
      this.$router.push('/signUp');
    },
  },
};
</script>


<style>
.login-top {
  width: 100%;
  height: 120px;
  padding-top: 1px;
  background-color: #e9e9e9;
}

.login-text1 {
  width: 100%;
  height: 20px;
  margin-top: 34px;
  font-size: 18px;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.5px;
  text-align: center;
  color: #585858;
}
.login-text2 {
  width: 100%;
  height: 16px;
  margin-top: 16px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.29;
  letter-spacing: -0.28px;
  text-align: center;
  color: #585858;
}

.login-content {
  width: 100%;
  height: 604px;
  padding: 0 16px;
  background-color: #fbfbfb;
}

.login-enter {
  height: 134px;
  width: 100%;
  margin-top: 24px;
}

.login-id {
  margin-bottom: 6px;
}

.login-pwd {
  margin-bottom: 24px;
}

.login-container .v-input__slot {
  height: 44px;
  width: 100% !important;
  padding-left: 12px;
  padding-right: 12px;
  padding-top: 0px;
  padding-bottom: 0px;
  border-radius: 6px;
  border: solid 1px #e1e1e1;
  background-color: #ffffff;
}

.login-container {
  padding-top: 24px;
  width: 100%;
}

.login-enter .v-text-field {
  font-family: NanumSquareR;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #c5c5c5;
}

.login-content .v-col .v-row {
  border-radius: 6px;
  border: solid 1px #e1e1e1;
  background-color: #ffffff;
}

.login-btns {
  margin-top: 0px;
}

.login-button {
  width: 100%;
  height: 44px;
  border-radius: 6px;
  border: solid 1px #ffd501;
  background-color: #ffd501;
  text-align: center;
  line-height: 44px;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.45px;
  color: #0d0d0d;
}

.login-create {
  width: 100%;
  height: 44px;
  border-radius: 6px;
  border: solid 1px #ffd501;
  background-color: #ffffff;
  margin-top: 6px;
  text-align: center;
  line-height: 44px;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.45px;
  color: #0d0d0d;
}

.login-find {
  margin-top: 16px;
  width: 100%;
  height: 16px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
}

.login-findid {
  width: 66px;
  height: 16px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.29;
  letter-spacing: -0.28px;
  text-align: left;
  color: #616161;
}

.login-findline {
  width: 2px;
  height: 16px;
  background-color: #e9e9e9;
  margin-left: 59px;
}

.login-findpwd {
  width: 78px;
  height: 16px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.29;
  letter-spacing: -0.28px;
  text-align: left;
  color: #616161;
  margin-left: 55px;
}

.s-header-layout-content {
  padding-top: 40px;
}

.login-password * {
  font-family: Arial, Helvetica, sans-serif !important;
}
</style>