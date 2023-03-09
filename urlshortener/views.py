from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import secrets

from .models import Url
from .serializers import UrlSerializer


def generate_shortened_url(length=6):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_link = ''.join(secrets.choice(alphabet) for _ in range(length))
    return new_link


class ShortenerAPIView(APIView):
    def post(self, request, pk):
        link = f'/api/ledger/{pk}/'
        new_link = generate_shortened_url()
        serializer = UrlSerializer(data={
            "link":link,
            "new_link":new_link})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class OriginalAPIView(APIView):
    def get(self, request, new_link):
        url = Url.objects.get(new_link=new_link)
        return HttpResponseRedirect(f'{url.link}')
