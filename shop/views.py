from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .serializers import ProductSerializer, CommentSerializer
from .models import Product, Comment


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
