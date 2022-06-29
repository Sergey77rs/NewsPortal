from django.urls import path
from .views import NewsList, OnenewsDetail


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', OnenewsDetail.as_view()),
]