from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from django.contrib.auth.hashers import make_password

# Create your tests here.
class SignUpViewTestCase(APITestCase):
    def setUp(self): # 매 테스트 전에 실행됨
        self.user = User(
            email="testuser1@test.com",
            password=make_password("dkssud!!"),
        )
        self.user.save()

    
    # 회원가입
    def test_signup_success(self):
        self.user_data = {
            "email": "testuser3@test.com",
            "password1": "dkssud!!",
            "password2": "dkssud!!",
        }
        
        self.signup_url = "/api/accounts/registration/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        
        # print("TestUser_test_signup_success : ", User.objects.all()) # PROCESS CHECK
        self.assertEqual(self.reponse.status_code, status.HTTP_201_CREATED)
    
    # 중복아이디 생성 오류
    def test_signup_id_check_fail(self): 
        self.user_data = {
            "email": "testuser1@test.com",# 중복아이디
            "password1": "dkssud!!",
            "password2": "dkssud!!",
        }
        self.signup_url = "/api/accounts/registration/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        self.assertEqual(self.reponse.status_code, status.HTTP_400_BAD_REQUEST) 

    # 비밀번호 오류
    def test_signup_password_check_fail(self):
        self.user_data = {
            "email":"testuser3@test.com", 
            "password1": "dkssud!!",
            "password2": "dkssud!!!",
        }
        self.signup_url = "/api/accounts/registration/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        self.assertEqual(self.reponse.status_code, status.HTTP_400_BAD_REQUEST) 


class SignInViewTestCase(APITestCase):
    # 로그인 존재하지 않는 아이디
    def test_login_no_username(self):
        self.login_url = "/api/accounts/login/"
        data = {
            "email":"testuser_not@test.com", 
            "password": "dkssud!!",
        } 
        response=self.client.post(self.login_url, data=data,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 비밀번호 불일치
    def test_password_fail(self):
        self.login_url = "/api/accounts/login/"
        data={
            "email":"testuser1@test.com", 
            "password": "dkssud!!!",
        }
        response=self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)