from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CommentViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]