from django.urls import path
from .views import CostBreakdownAPIView,NewsAPIView

urlpatterns= [

    path('calculate_price/', CostBreakdownAPIView.as_view(),name='calculate_price'),
    path('news/', NewsAPIView.as_view(),name='news'),

]