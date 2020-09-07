django-admin startproject mysite -> 프로젝트생성
python manage.py runserver -> 개발 서버 생성

기본으로 sqlite를 제공하는데 너무 느리니까 사용할 db로 바꾸는게 좋다고 해서
저번 프로젝트에서 쓰던 docker에 mariadb를 설치하여 시도하기로 했다.

docker : 
	database name : doginfo, 
	password : {catinfo}
