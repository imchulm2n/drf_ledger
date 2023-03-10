# 가계부 API


### 요구사항

a. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다.  
b. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다.   
c. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다.   
- 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다.   
- 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다.   
- 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.   
- 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다.   
- 가계부에서 상세한 세부 내역을 볼 수 있습니다.   
- 가계부의 세부 내역을 복제할 수 있습니다.  
- 가계부의 특정 세부 내역을 공유할 수 있게 단축 URL을 만들 수 있습니다.  
    (단축 URL은 특정 시간 뒤에 만료되어야 합니다.)  

로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.
## 유저 모델
- email 이메일
- password 패스워드

## 가계부 모델
- id
- date 날짜
- spent_money 지출
- earned_money 수입
- memo 메모
- balance 잔액

## API 명세서
1. http://127.0.0.1:8000/api/accounts/registration/  
POST : 회원가입  
2. http://127.0.0.1:8000/api/accounts/login/  
POST : 로그인  
3. http://127.0.0.1:8000/api/accounts/logout/  
POST : 로그아웃  
4. http://127.0.0.1:8000/api/ledger/  
GET : 목록 조회
POST : 세부 내역 생성
5. http://127.0.0.1:8000/api/ledger/{pk}/  
GET : 세부 내역 조회
PUT : 세부 내역 수정
DELETE : 세부 내역 삭제
6. http://127.0.0.1:8000/api/ledger/duplicate/{pk}/  
POST : 세부 내역 복제
7. http://127.0.0.1:8000/shortener/{pk}/  
POST : 단축 URL 생성
8. http://127.0.0.1:8000/{new_link}/  
GET : /ledger/<pk>/가 해당하는 URL로 이동

## a. 회원가입
http://127.0.0.1:8000/api/accounts/registration/  
POST 요청  

![image](https://user-images.githubusercontent.com/110436172/224178345-3f6b3921-9875-4ba5-b8bc-29a26fc549d2.png)


## b. 로그인
http://127.0.0.1:8000/api/accounts/login/  
POST 요청  

![image](https://user-images.githubusercontent.com/110436172/224178436-c170684b-1423-4eba-9536-40fee2883428.png)


## b. 로그아웃
http://127.0.0.1:8000/api/accounts/logout/  
POST 요청  

![image](https://user-images.githubusercontent.com/110436172/224178504-776bd19f-301e-458e-9efb-57b5ef80ab02.png)


## c. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다.   
## 0. 가계부 보기  
http://127.0.0.1:8000/api/ledger/  
GET요청  
1. 로그인 상태가 아닐 때, {"detail":"Authentication credentials were not provided."} 권한이 없다.  
![image](https://user-images.githubusercontent.com/110436172/224178939-64545a95-959a-400b-a11a-782b5c68e2c7.png)

2. 로그인 상태일 때,  
아직 내역이 추가되지 않아서 가계부가 비어있다.  
![image](https://user-images.githubusercontent.com/110436172/224178828-ecf5ab8c-1e68-4626-a9b8-741fb7a4f3e9.png)

## 1. 가계부 내역 추가
http://127.0.0.1:8000/api/ledger/  
POST 요청  
1. 첫 가계부 내역  
{  
    "date": "2023-03-01",   
    "spent_money": 0,  
    "earned_money": 50000,  
    "memo": "용돈",  
    "balance": 50000  
}  

![image](https://user-images.githubusercontent.com/110436172/224181329-4b09dc35-2fb7-4d39-b179-bbd2cef3bcc9.png)

2. 두번째 가계부 내역  
{  
    "date": "2023-03-01",  
    "spent_money": 20000,  
    "earned_money": 0,  
    "memo": "치킨"  
}  
balace:50000에서 지출 20000을 자동으로 계산해서 balace:30000으로 계산  
![image](https://user-images.githubusercontent.com/110436172/224181804-e933884b-b213-4f14-9136-a9cab9f08927.png)

3. 세번째 가계부 내역  
{  
    "date":"2023-03-01",  
    "spent_money":0,  
    "earned_money":50000,  
    "memo":"아르바이트트"  
}  
balace:30000에서 수입 20000을 자동으로 계산해서 balace:80000으로 계산
![image](https://user-images.githubusercontent.com/110436172/224182347-7adac736-cdf7-4f53-90b8-52cd0be0eaae.png)

## 2. 가계부 내역 수정
http://127.0.0.1:8000/api/ledger/3/  
PUT 요청  
세번째 가계부 내역에 오타(momo:아르바이트)가 있기 때문에 수정  
{ 
    "date":"2023-03-01",  
    "spent_money":0,  
    "earned_money":50000,  
    "memo":"아르바이트"  
} 
![image](https://user-images.githubusercontent.com/110436172/224182602-8c41ac9f-5922-42d9-ad1b-55703439a8ab.png)

## 3. 가계부 내역 삭제
http://127.0.0.1:8000/api/ledger/3/  
DELETE 요청  
![image](https://user-images.githubusercontent.com/110436172/224182700-76780000-90ce-4fca-98e0-91b1c9a84453.png)

## 4. 가계부 내역 조회
http://127.0.0.1:8000/api/ledger/  
GET요청  
추가한 내역(1,2)이 보이고 삭제한 내역(3)은 보이지 않는 것을 확인
![image](https://user-images.githubusercontent.com/110436172/224183109-0a0c5df3-b561-491d-a9b0-8fc6e3892746.png)

 
## 5. 가계부 세부 내역 조회
http://127.0.0.1:8000/api/ledger/1/  
GET 요청  
url에 마지막 /1/에 해당하는 가계부 세부 내역을 조회
![image](https://user-images.githubusercontent.com/110436172/224183329-c8233925-3b07-40f6-af8b-b932930e441a.png)

## 6. 가계부 세부 내역 복제
http://127.0.0.1:8000/api/ledger/duplicate/1/  
POST 요청  
url에 마지막 /1/에 해당하는 가계부 세부 내역을 복제

![image](https://user-images.githubusercontent.com/110436172/224183109-0a0c5df3-b561-491d-a9b0-8fc6e3892746.png)

/1/에 해당하는 세부 내역이 /4/에 새로 저장된 것을 확인
balance는 따로 계산
![image](https://user-images.githubusercontent.com/110436172/224183594-1474329b-8667-454d-9a34-555df25c678f.png)

## 7. 단축 URL 생성
http://127.0.0.1:8000/shortener/1/  
POST 요청  
/1/에 해당하는 url에 연결되는 단축 url 생성(/Gb9AIq/)  
(특정 시간 뒤에 만료하는 기능을 구현x) 
![image](https://user-images.githubusercontent.com/110436172/224183780-1d5f1559-db98-4210-9749-fa0eab488bbe.png)

http://127.0.0.1:8000/shortener/Gb9AIq/
GET 요청  
생성된 단축 URL로 이동하면 /1/에 해당하는 내역을 확인
![image](https://user-images.githubusercontent.com/110436172/224183881-c1d456f7-be04-4e65-b0ba-c845a1e6e57e.png)

## TestCase
python managy.py test --verbosity 3  
![image](https://user-images.githubusercontent.com/110436172/224205188-6c51b7e7-1cc3-458b-8e80-0ba928d45503.png)  
1. 회원가입
2. 중복 아이디 생성 오류
3. 비밀번호 오류
4. 존재하지 않는 아이디 로그인
5. 비밀번호 불일치
6. 가계부 목록 조회
7. 가계부 세부 내역 생성
8. 가계부 세부 내역 조회
9. 가계부 세부 내역 수정
10. 가계부 세부 내역 삭제

## Swagger 
http://127.0.0.1:8000/swagger/
1. accounts
![image](https://user-images.githubusercontent.com/110436172/224415366-411ffb90-8052-4956-be78-0a98090fbe1a.png)
2. ledger
![image](https://user-images.githubusercontent.com/110436172/224415456-d34e6325-e8c8-4e3a-98d8-e930f01632a3.png)
3. shortener
![image](https://user-images.githubusercontent.com/110436172/224415539-ca406763-cc2f-4b92-83e6-763accaf7e8f.png)
4. models
![image](https://user-images.githubusercontent.com/110436172/224415626-3c6d08c8-beac-4f8d-8e93-409682006aca.png)

## Redoc
http://127.0.0.1:8000/redoc/
![image](https://user-images.githubusercontent.com/110436172/224416075-0387d4c0-006a-4954-b7bb-2b41267acc08.png)

