from django.urls import path

from .views import LedgersAPIView, LedgerDetailAPIView, LedgerDuplicateView

urlpatterns = [
    path('ledger/', LedgersAPIView.as_view()),
    path('ledger/<int:pk>/', LedgerDetailAPIView.as_view()),
    path('ledger/duplicate/<int:pk>/', LedgerDuplicateView.as_view()),
]