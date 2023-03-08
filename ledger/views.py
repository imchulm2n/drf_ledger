from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

from .models import Ledger
from .serializers import LedgerSimpleSerializer, LedgerDetailSerializer, LedgerCreateSerializer
from .permissions import IsAuthenticated


# Create your views here.
class LedgersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # 게시글 목록 확인
    def get(self, request):
        ledgers = Ledger.objects.all()
        serializer = LedgerSimpleSerializer(ledgers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # 게시글 생성
    def post(self, request):
        serializer = LedgerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LedgerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # 게시글 확인
    def get(self, request, pk):
        ledger = get_object_or_404(Ledger, id=pk)
        serializer = LedgerDetailSerializer(ledger)
        print(ledger)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 수정
    def put(self, request, pk):
        ledger = get_object_or_404(Ledger, id=pk)
        serializer = LedgerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 게시글 삭제
    def delete(self, request, pk):
        ledger = get_object_or_404(Ledger, id=pk)
        if ledger is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            ledger_object = Ledger.objects.get(id=pk)
            ledger_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)


# 게시글 복제
class LedgerDuplicateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            ledger_to_duplicate = Ledger.objects.get(id=pk)
        except Ledger.DoesNotExist:
            return Response({"message": "Post not found"}, status=404)
        print(ledger_to_duplicate)
        serializer = LedgerCreateSerializer(data={
            "spent_money":ledger_to_duplicate.spent_money,
            "memo":ledger_to_duplicate.memo,
            "day":ledger_to_duplicate.day
        })

        if serializer.is_valid():      
            new_ledger = serializer.save()
            new_ledger.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

