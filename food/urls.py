from . import views
from django.urls import path
app_name= 'food'
urlpatterns= [
    path('',views.IndexClassView.as_view(),name='index'),
    path('items/',views.items,name='items'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('add/',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
]