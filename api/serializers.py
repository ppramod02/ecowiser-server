from django.contrib.auth.models import User
from .models import Brand, Product
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class BrandSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creator_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField
    logo = serializers.CharField()  # base64 image

    class Meta:
        model = Brand
        fields = ['id', 'creator_id', 'name', 'description', 'logo']

    def create(self, validated_data):
        brand = Brand.objects.create(
            creator_id=validated_data['creator_id'],
            name=validated_data['name'],
            description=validated_data['description'],
            logo=validated_data['logo']
        )
        return brand
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Brand` instance, given the validated data.
        """
        instance.creator_id = validated_data.get('creator_id', instance.creator_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        return instance
    

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    creator_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField
    category = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.CharField()
    brand_id = serializers.IntegerField()
    stock = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id', 'creator_id', 'name', 'description', 'category', 'price', 'image', 'brand_id', 'stock']

    def create(self, validated_data):
        product = Product.objects.create(
            creator_id=validated_data['creator_id'],
            name=validated_data['name'],
            description=validated_data['description'],
            category=validated_data['category'],
            price=validated_data['price'],
            image=validated_data['image'],
            brand_id=validated_data['brand_id'],
            stock=validated_data['stock'],
        )
        return product
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Brand` instance, given the validated data.
        """
        instance.creator_id = validated_data.get('creator_id', instance.creator_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.brand_id = validated_data.get('brand_id', instance.brand_id)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance
