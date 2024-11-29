
from django.urls import path, include
from rest_framework import routers
from reviews import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'business', views.BusinessViewSet)
router.register(r'category', views.CategoryViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),   
]
