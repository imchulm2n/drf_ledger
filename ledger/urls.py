from django.urls import path

from .views import LedgersAPIView, LedgerAPIView, LedgerDuplicateView

urlpatterns = [
    path('ledger/', LedgersAPIView.as_view()),
    path('ledger/<int:pk>/', LedgerAPIView.as_view()),
    path('ledger/duplicate/<int:pk>/', LedgerDuplicateView.as_view()),
]