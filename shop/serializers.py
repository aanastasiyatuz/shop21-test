from rest_framework import serializers

from .models import Product, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        return rep

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = instance.user.username
        return rep

