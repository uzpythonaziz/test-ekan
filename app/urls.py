from django.urls import path
from .views import *
urlpatterns = [
     path('api/v1/allproduct',AllProduct.as_view()),
     path('api/v1/allcategory',AllCategory.as_view()),
     path('api/v1/detail/<int:id',DetailProduct.as_view()),
    #  path('api/v1/detailwith/<str:name>',DetailwithProduct.as_view()),
     path('api/v1/ctegorydetail/<int:id',DetailCategory.as_view()),     
     
 ]
 