from django.urls import path

from . import views

urlpatterns = [
    path('catalog/', views.get_catalog, name="catalog"),
    # path('catalog/<slug:catalog_slug>/', views.get_categories_by_catalog, name="get_categories_by_catalog"),
    path('catalog/<slug:catalogSlug>/', views.get_products_by_catalog, name="get_products_by_catalog"),

    path('categories/', views.get_categories, name="categories"),
    path('products/', views.get_products, name="products"),
    path('products/<str:pk>/', views.get_product, name="product"),
    path('categories/<slug:category_slug>/create/',
         views.create_product_by_category, name='create_product_by_category'),
    path('categories/<slug:category_slug>/upload/',
         views.upload_image_by_category, name='upload_image_by_category'),
    path('categories/<slug:category_slug>/', views.get_products_by_category,
         name='products_by_category'),
    path('categories/<slug:category_slug>/<slug:product_slug>/reviews/',
         views.createProductReview, name='create-review'),
    path('categories/<slug:category_slug>/<slug:product_slug>/',
         views.get_product_by_category, name='get_product_by_category'),
    path('categories/<slug:category_slug>/update/<slug:product_slug>/',
         views.update_product_by_category, name="update_product_by_category"),
    path('categories/<slug:category_slug>/delete/<slug:product_slug>/',
         views.delete_product_by_category, name="delete_product_by_category"),

    path('users/', views.getUsers, name="users"),
    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/profile/update/', views.updateUserProfile,
         name="user-profile-update"),
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),

    path('users/<str:pk>/', views.getUserById, name='user'),
    path('users/update/<str:pk>/', views.updateUser, name='user-update'),
    path('users/delete/<str:pk>/', views.deleteUser, name='user-delete'),

    path('orders/', views.getOrders, name='orders'),
    path('orders/add/', views.addOrderItems, name='orders-add'),
    path('orders/myorders/', views.getMyOrders, name='myorders'),
    path('orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
    path('orders/<str:pk>/', views.getOrderById, name='user-order'),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
