from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('shoppingitems/<int:pk>', views.shoppingitemsDetailView.as_view(), name = 'shoppingitem_detail'),
    path('shoppingitems/', views.shoppingitemsListView.as_view(), name = 'shoppingitems'),
   ]

