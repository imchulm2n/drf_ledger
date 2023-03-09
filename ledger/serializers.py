from rest_framework import serializers

from .models import Ledger


class LedgerSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('id', 'date', 'spent_money', 'earned_money', 'memo', 'balance')


class LedgerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ('id', 'date', 'spent_money', 'earned_money', 'memo', 'balance')


class LedgerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ledger
        fields = ('id', 'date', 'spent_money', 'earned_money', 'memo', 'balance')
