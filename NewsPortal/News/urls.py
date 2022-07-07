from django.urls import path
from .views import NewsList, OnenewsDetail, SearchList, AddCreate, NewsEdit, NewsDelete


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', OnenewsDetail.as_view(), name='onenews'),
   path('search/', SearchList.as_view(), name='search'),
   path('add/', AddCreate.as_view(), name='add'),
   path('<int:pk>/edit', NewsEdit.as_view(), name='edit'),
   path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),
]