from django.urls import path
from .views import HomeView, FetchNewsView, LatestNewsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fetch-news/', FetchNewsView.as_view(), name='fetch-news'),
    path('latest-news/', LatestNewsView.as_view(), name='latest-news'),

]
