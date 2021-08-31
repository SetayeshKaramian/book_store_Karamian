from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(),
         name='book_detail'),
    path('search', SearchResultListView.as_view(), name="search_results"),
]
