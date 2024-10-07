from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView
from api import views


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('brands/', views.brand_list),
    path('brand/<int:pk>/', views.brand_detail),
    path('brands/search/', views.brand_search),
    path('products/', views.product_list),
    path('product/<int:pk>/', views.product_detail),
    path('products/search/', views.product_search),
    path('data/<int:id>/', views.data_by_creator),
    # TODO: add urls for search through brand name, product name, category 
]
