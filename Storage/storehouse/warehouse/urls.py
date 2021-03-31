from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register(r'order', views.OrderViewSet)
router.register(r'order_item', views.OrderItemViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]