<h1 align="center">소개해듀개 🐶</h1>

![PowerPoint 슬라이드 쇼 -  소개해듀개  2020-10-08 오전 11_11_54](https://user-images.githubusercontent.com/50106311/95407593-68812c00-0958-11eb-8823-d648898edb11.png)

## 📎 프로젝트 소개 

#### 자신에게 맞는 유기견을 소개해 주는 모바일 웹사이트
 매해 유기되는 동물의 수는 10만마리 이상으로 높은 수치를 기록하고 있습니다.
**작년 유기동물 구조수는 13만 5천 791마리**로 전년 대비 12%나 증가한 수치를 보이고 있습니다.
유기견의 숫자가 늘어날 수록 최근 많은 미디어에서는 **사지말고 입양하세요** 라는 캠페인을 벌이는 사람들이 늘어나고 있습니다.
이렇듯 사회에서 유기견에 대한 관심이 높아졌고 저희 팀은 **유기견과 관련된 프로젝트**를 진행하고자 하였습니다.

# 🐾 Main Feature
### 자신과 잘 맞는 강아지를 매칭
![PowerPoint 슬라이드 쇼 -  소개해듀개  2020-10-08 오전 11_45_53](https://user-images.githubusercontent.com/50106311/95409089-e430a800-095b-11eb-9119-c0b0656bf50d.png)

  **소개해듀개**🐩는 **유기견 매칭 서비스**와 **잃어버린 강아지를 찾아주는** 플랫폼입니다. 
  
 기존의 강아지 매매 시장에서 벗어나 강아지를 입양하고 싶은 이용자에게 유기견을 추천해 줍니다. 이용자의 생활 조건과 강아지의 특성 데이터를 바탕으로 분석하여 추천 시스템을 구현하였습니다. 강아지를 입양하기를 바라지만 자신이 맞지 않는 사람일까 걱정하는 이용자에게 알맞은 강아지를 추천하면서 유기된 동물을 보호하고 이용자도 만족할 수 있도록 합니다. 

 또한 유기견 중에 자신이 잃어버린 강아지가 있을 수 있습니다. 유기견 중에 자신의 강아지를 찾기 힘든
  애견인을 위한 서비스로 잃어버린 강아지 찾기 서비스를 구현하였습니다. 강아지 이미지 분석을 통해 유사한 강아지를 잃어버린 장소에 따라 보여주며 유기견이 주인의 품으로 돌아가게 만들 수 있습니다. 
 
 이 외에도 내 주변에 있는 강아지들을 확인하며 입양의 꿈을 키울 수도 있고, 나의 사진과 닮은 강아지는 어떤 강아지를 보여주면서 기존의 유기견 플랫폼과의 차별점을 두었습니다. 

 - 나와 어울리는 멍멍이 매칭
 - 잃어버린 멍멍이 찾기
 - 내 주변 멍멍이 보기 
 - 나와 닯은 멍멍이 찾기

## 📚 프로젝트 산출물 

- [프로젝트개발문서](https://docs.google.com/spreadsheets/d/1LEYeqWii-0VhSPL8beeVzDFWaB1xnoXN_eX04GQBbzY/edit#gid=0)

## 기술 스택

## 기술 설명 

### ERD 
![ERD](https://cdn.discordapp.com/attachments/749825922936602695/755349369066094672/unknown.png)
### API Document
 - 회원

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT|
|-------|-----------|---------------|----------| 
|POST	|/accounts/signup	|회원가입	|"사용자 이름 이메일 패스워드"|
|POST	|/accounts/profile	|회원가입할 때 사용자 사진 업로드 받기|	사용자 사진|
|POST	|/accounts/login	|로그인	|"이메일 패스워드"|
|POST	|/accounts/logout	|로그아웃	|-|
|GET	|/accounts/islogin	|백에서 세션 있는지 확인|-|
|GET	|/accounts/mypage	|유저 프로필 보기|-|
 - 메인화면

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|POST	|/filters	|필터가 적용된 리스트 보이기	|필터 내용들.. (단모, 색깔.. 등등)	|강아지들 리스트|


 - 나와 어울리는 멍멍이 찾기

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|
|-------|-----------|---------------|-----------|
|POST	|/matches	|나와 어울리는 멍멍이 조건들 입력하기	|"사진 들 중 귀엽다 생각한 멍멍이들 id 여러개 배열필터에 들어간 조건들 (사용자 성격, 환경 등등)"||	
|GET	|/matches	|나와 어울리는 멍멍이 결과 출력하기		|"멍멍이 사진 멍멍이 정보들 (나이, 몸무게, 성별, 종, 색깔, 중성화 여부, 특징, 발견장소, 발견날짜, 공고 끝나는 날짜) 유기소 정보들 (보호소 이름, 위치, 전화번호, 관리자)"|


 - 잃어버린 멍멍이 찾기

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|POST	|/losts	|잃어버린 멍멍이 사진 업로드 받기	|멍멍이 사진	
|GET	|/losts/{my_location}	|내 위치 유기 멍멍이들 리스트 받기		|-|"간략한 강아지 정보들 (사진, 이름) => 누르면 자세히 보기로 감"|
|PUT	|/losts	|위치 검색해서 수정된 멍멍이 리스트 받기	|검색하고싶은 위치	|"간략한 강아지 정보들 (사진, 이름) => 누르면 자세히 보기로 감"|


 - 내 주변 멍멍이 찾기

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|GET	|/arounds	|내 위치 기준 보호소 정보 받기		||위도, 경도, 보호소 이름
|POST	|/arounds	|보호소 이름 받으면 그 보호소 내 멍멍이 리스트|보호소 이름	|"간략한 강아지 정보들(사진, 이름) => 누르면 자세히 보기로 감"|

 - 나와 닮은 멍멍이 찾기

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|POST	|/resemblances	|내 이미지 업로드하기	|내 이미지	|
|GET	|/resemblances/{progile_img}	|그 이미지와 어울리는 강아지 정보 주기|		"강아지 사진"|


 - 관심 있는 멍멍쓰

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|POST	|/likes	|관심 멍멍 누르기	|유기동물 접수 번호 (dog_id)||
|GET	|/likes	|관심 멍멍 리스트	|	|멍멍이 사진, 정보, 유기소 정보|


 - 공통화면 

|METHOD	|RESOURCE	|DESCRIPTION	|예상 INPUT	|예상 OUTPUT|
|-------|-----------|---------------|-----------|-----------|
|GET	|/details/{dog_id}	|멍멍이 자세히 보기||멍멍이 사진, 정보, 유기소 정보|

# FRONTEND

```sh
cd sub2/frontend
npm install
npm run serve
```

# BACKEND

```sh
cd backend/introducedog/introducedog
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

# DATA

## Author 

 🙋 **Kim Chaeun**
 - Gitlab : @fairy037

 💁 **Seo Seughee**
 - Gitlab : @pucca94

 🙆 **Jeon Soyun**
 - Gitlab :  @twoposition 

 🙎 **Choi Jin**
 - Gitlab :  @choi_jin