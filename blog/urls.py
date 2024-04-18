from django.urls import path
from .views import DetailedCostBreakdownAPIView,NewsAPIView,NewsDetailAPIView,ReviewAPIView,BannerAPIView,UserCountAPIView

urlpatterns= [

    path('calculate_price/', DetailedCostBreakdownAPIView.as_view(),name='calculate_price'),
    path('news/', NewsAPIView.as_view(),name='news'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(),name='news_detail'),
    path('review/', ReviewAPIView.as_view(),name='review'),
    path('banner/', BannerAPIView.as_view(),name='banner'),
    path('user_count/', UserCountAPIView.as_view(),name='user_count'),
]