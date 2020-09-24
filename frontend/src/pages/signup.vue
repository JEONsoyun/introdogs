<template>
  <s-main-layout title="회원가입" noArrow>
    <div class="signup-page">
      <div class="signup-page-title">이름</div>
      <v-text-field
        v-model="data.memberName"
        placeholder="이름 입력"
        class="signup-page-box"
        dense
        required
        hide-details
        outlined
      ></v-text-field>
      <div class="signup-page-title">이메일 (ID)</div>
      <v-text-field
        v-model="data.memberEmail"
        placeholder="이메일 입력 (예: introdogs@introdogs.com)"
        class="signup-page-box"
        dense
        required
        hide-details
        outlined
      ></v-text-field>
      <div class="signup-page-title">비밀번호</div>
      <v-text-field
        type="password"
        class="signup-page-box"
        v-model="data.memberPw"
        dense
        hide-details
        required
        placeholder="비밀번호 입력 (8자 이상의 영문,특수문자를 조합)"
        counter
        outlined
      ></v-text-field>
      <div class="signup-page-title">비밀번호 확인</div>
      <v-text-field
        class="signup-page-box"
        type="password"
        placeholder="비밀번호 확인"
        v-model="data.memberPwVerification"
        dense
        required
        hide-details
        outlined
      ></v-text-field>

      <s-button style="margin-top:24px;" @click="onSignupClick">회원가입</s-button>
    </div>
  </s-main-layout>
</template>

<script>
export default {
  name: 'signup-page',
  data: () => ({
    data: {}
  }),
  methods: {
    async onSignupClick() {
      try {
        const memberName = this.data.memberName;
        const memberEmail = this.data.memberEmail;
        const memberPw = this.data.memberPw;
        const memberPwVerification = this.data.memberPwVerification;
        let memberBirth = `${this.data.year}-${this.data.month}-${this.data.day}`;
        const teamIdx = this.data.teamIdx;

        // 0. 이름 체크
        if (!memberName || memberName.trim().length == 0) {
          return alert('이름을 입력해주세요.');
        }

        // 1. 이메일 체크
        if (!memberEmail || memberEmail.trim().length == 0) {
          return alert('이메일 주소를 입력해주세요.');
        }

        let checkEmailResult = await this.$api.postEmail({ memberEmail });

        if (checkEmailResult.data.status != 200) {
          return alert(
            '이미 사용중인 이메일입니다. 다른 이메일 주소를 입력해주세요.'
          );
        }

        // 2. 이름 체크
        if (!memberName || memberName.trim().length == 0) {
          return alert('이름을 입력해주세요.');
        }

        // 3. 비밀번호 체크
        if (!memberPw || memberPw.trim().length == 0) {
          return alert('비밀번호를 입력해주세요.');
        }

        if (memberPw != memberPwVerification) {
          return alert('비밀번호가 일치하지 않습니다.');
        }

        // 4. 약관 동의 체크
        if (!this.data1.checkbox) {
          return alert('약관에 동의해야 회원가입이 가능합니다.');
        }

        // 5. 생일 체크
        if (!this.data.year && !this.data.month && !this.data.day) {
          memberBirth = null;
        }

        await this.$api.postsignup({
          memberEmail,
          memberPw,
          memberName,
          memberBirth,
          teamIdx,
        });

        this.$router.push('/');
      } catch (e) {
        console.error(e);
      }
    },
    async postEmail() {
      try {
        const memberEmail = this.data.memberEmail;
        const post = {
          memberEmail,
        };
        let tmp = await this.$api.postEmail(post);
        console.log(tmp.data.message);
      } catch (e) {
        console.error(e);
      }
    },
  },
};
</script>

<style>
.signup {
  width: 100%;
  height: 40px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.29;
  text-align: center;
  color: #585858;
  background-color: #ffffff;
  position: fixed;
  top: 48px;
  left: 0px;
}

.signup-page-title {
  width: 80%;
  height: 16px;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #616161;
  margin-bottom: 10px;
  margin-top: 25px;
  margin-left: 4%;
}

.signup-page .v-text-field input {
  font-family: Binggrae;
}
.signup-page-password {
  width: 100%;
  height: 44px;
  border-radius: 4px;
  border: solid 1px #e1e1e1;
  background-color: #ffffff;
  margin-bottom: 18px;
  padding-left: 12px;
  font-size: 14px;
  font-family: serif;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #1e1e1e;
}
.signup-page .v-label theme--light {
  font-size: 14px;
  color: #616161;
  font-weight: 400;
}

.signup-page {
  margin-top: 24px;
  margin-left: 3%;
  margin-right: 3%;
  margin-bottom: 18px;
}

.signup-page-birth {
  width: 30%;
  height: 44px;
  border-radius: 4px;
  border: solid 1px #e1e1e1;
  background-color: #ffffff;
  margin-bottom: 18px;
  margin-right: 3%;
  margin-left: 3%;
  padding-left: 12px;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #1e1e1e;
}

.signup-page-slash {
  width: 9px;
  height: 26px;
  font-size: 24px;
  font-weight: 400;
  line-height: 0.75;
  letter-spacing: -0.67px;
  text-align: left;
  color: #c5c5c5;
  margin-top: 1.5%;
  margin-left: 2%;
  margin-right: 2%;
}

.signup-page-select {
  padding-top: 0px;
}

.signup-page-selectbox {
  margin-top: 0px;
  width: 50%;
  height: 44px;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.29;
  letter-spacing: -0.39px;
  text-align: left;
  color: #1e1e1e;
}
.signup-page-line {
  margin-top: 24px;
  margin-bottom: 29px;
  width: 100%;
  height: 0.1px;
  background-color: #e9e9e9;
}

.signup-page-right {
  width: 10%;
  margin-left: 5%;
  margin-bottom: 20px;
}
.signup-page-left {
  width: 90%;
  margin: 0px 5% 0px 0px;
  border-left: 10%;
}
.signup-page-title1 {
  width: 80%;
  font-size: 14px;
  font-weight: 700;
  line-height: 24px;
  margin-left: 8px;
  color: #616161;
}

.signup-page-agree-content {
  width: 90%;
  margin-left: 32px;
  height: 53px;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.5;
  letter-spacing: -0.34px;
  text-align: left;
  color: #a5a5a5;
}
.s-header-layout-content {
  padding-top: 40px;
}

.signup-page-box input {
  padding: 0 !important;
}
.signup-page-box .v-input__control {
  height: 44px !important;
}

.signup-page-box .v-text-field__slot {
  height: 44px;
  font-size: 14px;
  color: #8a8a8a !important;
}
.signup-page-box fieldset {
  border-color: #e1e1e1 !important;
  height: 48px;
  background: #fff;
}

.signup-page-selectbox fieldset {
  border-color: #e1e1e1 !important;
  height: 48px;
  border-width: 0.1px !important;
  background: #fff;
}

.signup-page-line {
  border-color: #e9e9e9 !important;
}
</style>
