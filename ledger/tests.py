from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.hashers import make_password

from accounts.models import User
from .models import Ledger

import json
# Create your tests here.
class LedgerViewTestCase(APITestCase):
    def setUp(self): # 매 테스트 전에 실행됨
        self.user = User(
            email="testuser1@test.com",
            password=make_password("dkssud!!"),
        )
        self.user.save()

        self.ledger = Ledger(
            date = "2023-03-01",
            spent_money= 0,
            earned_money= 30000,
            memo= "hi",
            balance= 30000
        )
        self.ledger.save()

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    
    # 가계부 목록 조회
    def test_ledger_list(self):
        self.ledgers_url = "/api/ledger/"
        self.reponse = self.client.get(self.ledgers_url)
        
        self.assertEqual(self.reponse.status_code, status.HTTP_200_OK)
    
    # 가계부 내역 생성
    def test_ledger_create(self):
        self.ledgers_url = "/api/ledger/"
        
        ledger = {
            "date": "2023-03-01",
            "spent_money": 0,
            "earned_money": 20000,
            "memo": "hi",
            "balance": 20000,
            }

        self.reponse = self.client.post(self.ledgers_url, ledger, format="json")

        self.assertEqual(self.reponse.status_code, status.HTTP_201_CREATED)


    # 가계부 세부 내역 조회
    def test_ledger_list(self):
        last_instance = Ledger.objects.last()
        ledger_id = last_instance.id
        self.ledger_url = f"/api/ledger/{ledger_id}/"
        self.reponse = self.client.get(self.ledger_url)
        
        self.assertEqual(self.reponse.status_code, status.HTTP_200_OK)


    # 가계부 세부 내역 수정
    def test_ledger_put(self):
        last_instance = Ledger.objects.last()
        ledger_id = last_instance.id
        self.ledger_url = f"/api/ledger/{ledger_id}/"
        
        ledger = {
            "date": "2023-03-01",
            "spent_money": 10000,
            "earned_money": 0,
            "memo": "hello",
            }
        
        self.reponse = self.client.put(self.ledger_url, ledger, format="json")
        
        self.assertEqual(self.reponse.status_code, status.HTTP_201_CREATED)


    # 가계부 세부 내역 삭제
    def test_ledger_delete(self):
        last_instance = Ledger.objects.last()
        ledger_id = last_instance.id
        self.ledger_url = f"/api/ledger/{ledger_id}/"
        self.reponse = self.client.delete(self.ledger_url)
        
        self.assertEqual(self.reponse.status_code, status.HTTP_200_OK)
