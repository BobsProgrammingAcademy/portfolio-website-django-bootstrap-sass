from django.urls import path
from .views import IndexPageView

urlpatterns = [
  path('', IndexPageView.as_view()),
]
