from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Brand, Product
from .serializers import RegisterSerializer, BrandSerializer, ProductSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@csrf_exempt
def brand_list(request):
    """
    List all products, or create a product.
    """
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def brand_detail(request, pk):
    """
    Retrieve, update or delete a brand.
    """
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(brand, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        brand.delete()
        Product.objects.filter(brand_id=pk).delete()
        return HttpResponse(status=204)
    
@csrf_exempt
def brand_search(request, name):
    """
    Retrieve products of a brand.
    """
    try:
        brand = Brand.objects.filter(name__istartswith=name)
        brand_ids = brand.values_list('id', flat=True)
    except Brand.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        products = Product.objects.filter(brand_id__in=brand_ids)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def data_by_creator(request, id):
    """
    Retrieve products and brands using creator.
    """
    try:
        brands = Brand.objects.filter(creator_id=id)
        products = Product.objects.filter(creator_id=id)
    except Brand.DoesNotExist or Product.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        prod_serializer = ProductSerializer(products, many=True)
        brand_serializer = BrandSerializer(brands, many=True)
        return JsonResponse({ 'brands': brand_serializer.data, 'products': prod_serializer.data }, safe=False)

@csrf_exempt
def product_list(request):
    """
    List all products, or create a product
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a product
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)