from django.http.response import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create_order/",views.create_order,name="create_order"),
    path("update_order/<str:pk_id>/",views.update_order, name="update_order"),
    path('remove_order/<str:pk>/',views.remove_order, name="remove_order"),
    path("product_view/<str:pk>/",views.Product_view,name="product_view")
]
