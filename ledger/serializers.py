from rest_framework import serializers
from .models import Ledger



class LedgerSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('id', 'spent_money', 'memo', 'day')


class LedgerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('id', 'spent_money', 'memo', 'day')


class LedgerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('spent_money', 'memo', 'day')
