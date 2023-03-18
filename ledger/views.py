from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ledger
from api.permissions import IsOwner
from .serializers import LedgerSimpleSerializer, LedgerCreateSerializer, LedgerDetailSerializer

class LedgersAPIView(APIView):
    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        try:
            object = Ledger.objects.get(id=obj_id)
        except Ledger.DoesNotExist:
            return

        self.check_object_permissions(self.request, object)
        return object


    # 게시글 목록 확인
    def get(self, request):
        ledgers = Ledger.objects.all()
        serializer = LedgerSimpleSerializer(ledgers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # 게시글 생성
    def post(self, request):
        last_instance = Ledger.objects.last()
        if last_instance == None:
            serializer = LedgerCreateSerializer(data={
                "date":request.data.get('date'),
                "spent_money":request.data.get('spent_money'),
                "earned_money":request.data.get('earned_money'),
                "memo":request.data.get('memo'),
                "balance":request.data.get('earned_money')
            }
            )
        else:
            serializer = LedgerCreateSerializer(data={
                "date":request.data.get('date'),
                "spent_money":request.data.get('spent_money'),
                "earned_money":request.data.get('earned_money'),
                "memo":request.data.get('memo'),
                "balance":int(last_instance.balance) - int(request.data.get('spent_money')) + int(request.data.get('earned_money')),
            }
            )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class LedgerDetailAPIView(APIView):
    permission_classes = [IsOwner]
    
    def get_object_and_check_permission(self, obj_id):
        try:
            object = LedgerDetailSerializer.objects.get(id=obj_id)
        except Ledger.DoesNotExist:
            return

        self.check_object_permissions(self.request, object)
        return object
    
    # 게시글 확인
    def get(self, request, pk):
        ledger = get_object_or_404(Ledger, id=pk)
        serializer = LedgerDetailSerializer(ledger)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    # 게시글 수정
    def put(self, request, pk):
        ledger = get_object_or_404(Ledger, id=pk)
        serializer = LedgerDetailSerializer(ledger, data=request.data)
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
    permission_classes = [IsOwner]

    def post(self, request, pk):
        try:
            ledger_to_duplicate = Ledger.objects.get(id=pk)
        except Ledger.DoesNotExist:
            return Response({"message": "Post not found"}, status=404)
        
        
        last_instance = Ledger.objects.last()
        serializer = LedgerDetailSerializer(data={
            "date":ledger_to_duplicate.date,
            "spent_money":ledger_to_duplicate.spent_money,
            "earned_money":ledger_to_duplicate.earned_money,
            "memo":ledger_to_duplicate.memo,
            "balance":int(last_instance.balance) - int(ledger_to_duplicate.spent_money) + int(ledger_to_duplicate.earned_money),
        })

        if serializer.is_valid():      
            new_ledger = serializer.save()
            new_ledger.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
