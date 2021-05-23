from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime


from .models import Catalog, Category, Product, Order, OrderItem, ShippingAddress, Review
from .serializers import CatalogSerializer, CategorySerializer, ProductSerializer, UserSerializer, UserSerializerWithToken, OrderSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    if data['password'] != '':
        user.password = make_password(data['password'])
    user.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']
    user.save()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')


@api_view(['GET'])
def get_catalog(request):
    catalog = Catalog.objects.all()
    serializer = CatalogSerializer(catalog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories_by_catalog(request, catalog_slug):
    catalog = None
    products = Product.objects.all()
    if catalog_slug:
        catalog = Catalog.objects.get(catalog_slug=catalog_slug)
        categoriesAfterFilter = products.filter(catalog_id=catalog.id)
    serializer = CategorySerializer(categoriesAfterFilter, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,
                                   many=True)  # установив many=True , вы сообщаете drf, что queryset содержит несколько элементов (список элементов), поэтому drf должен сериализовать каждый элемент с помощью класса serializer (и serializer.data будет списком). если вы не зададите этот аргумент, это означает, что queryset-это один экземпляр, а serializer.data - один объект)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product deleted')


@api_view(['GET'])
def get_products_by_category(request, category_slug):
    category = None
    products = Product.objects.all()
    if category_slug:
        category = Category.objects.get(category_slug=category_slug)
        productsAfterFilter = products.filter(category_id=category.id)
    serializer = ProductSerializer(productsAfterFilter, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_category(request, category_slug, product_slug):
    product = None
    if category_slug and product_slug:
        product = Product.objects.get(product_slug=product_slug)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product_by_category(request, category_slug):
    user = request.user
    product = None
    if category_slug:
        product = Product.objects.create(
            user=user,
            name='Sample Name',
            product_slug='sampleslug',
            description='',
            price=0,
            count_in_stock=0,
            category_id_id=1
        )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product_by_category(request, category_slug, product_slug):
    product = None
    if category_slug and product_slug:
        data = request.data
        product = Product.objects.get(product_slug=product_slug)
        product.name = data['name']
        product.product_slug = data['product_slug']
        product.description = data['description']
        product.rating = data['rating']
        product.num_reviews = data['num_reviews']
        product.price = data['price']
        product.count_in_stock = data['count_in_stock']
        product.code = data['code']
        product.color_frame = data['color_frame']
        product.color_mirror = data['color_mirror']
        product.base_mirror = data['base_mirror']
        product.height = data['height']
        product.width = data['width']
        product.weight = data['weight']
        product.type_of_installation = data['type_of_installation']
        product.type_of_mounting = data['type_of_mounting']
        product.heightWithoutFrame = data['heightWithoutFrame']
        product.weightWithoutFrame = data['weightWithoutFrame']
        product.faced = data['faced']
        product.form = data['form']
        product.appointment = data['appointment']
        product.material_mirror = data['material_mirror']
        product.material_frame = data['material_frame']
        product.country_brand = data['country_brand']
        product.country_manufacturer = data['country_manufacturer']
        product.manufacturer = data['manufacturer']
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product_by_category(request, category_slug, product_slug):
    product = None
    if category_slug and product_slug:
        product = Product.objects.get(product_slug=product_slug)
    product.delete()
    return Response('Product deleted')


@api_view(['POST'])
def upload_image_by_category(request, category_slug):
    if category_slug:
        data = request.data
        product_slug = data['product_slug']
        product = Product.objects.get(product_slug=product_slug)
        product.image = request.FILES.get('image')
        product.save()
    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'},
                        status=status.HTTP_400_BAD_REQUEST)
    else:

        # (1) Create order

        order = Order.objects.create(
            user=user,
            payment_method=data['paymentMethod'],
            tax_price=data['taxPrice'],
            shipping_price=data['shippingPrice'],
            total_price=data['totalPrice']
        )

        # (2) Create shipping address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postal_code=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            product = Product.objects.get(id=i['id'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['quantity'],
                price=i['price'],
                image=product.image.url,
            )

            # (4) Update stock

            product.count_in_stock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):
    user = request.user

    try:
        order = Order.objects.get(id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response({'detail': 'Not authorized to to view this order'},
                     status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Order does not exist'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(id=pk)
    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()
    return Response('Order was paid')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(id=pk)
    order.is_delivered = True
    order.delivered_at = datetime.now()
    order.save()
    return Response('Order was delivered')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, category_slug, product_slug):
    if category_slug:
        user = request.user
        product = Product.objects.get(product_slug=product_slug)
        data = request.data
        alreadyExists = product.review_set.filter(user=user).exists()
        if alreadyExists:
            content = {'detail': 'Product already reviewed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif data['rating'] == 0:
            content = {'detail': 'Please select a rating'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            review = Review.objects.create(
                user=user,
                product=product,
                name=user.first_name,
                rating=data['rating'],
                comment=data['comment'],
            )
            reviews = product.review_set.all()
            product.num_reviews = len(reviews)
            total = 0
            for i in reviews:
                total += i.rating
                product.rating = total / len(reviews)
            product.save()
    return Response('Review Added')