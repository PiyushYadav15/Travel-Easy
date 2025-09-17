from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('create_category', views.create_category,name='create_category'),
    path('catrgory_list', views.category_list,name='category_list'),
    path('photo_create',views.photo_create,name='photo_create'),
    path('photo_list',views.photo_list,name='photo_list'),
    path('photo_update/<int:pid>', views.photo_update, name='photo_update'),
    path('photo_delete/<int:pid>', views.photo_delete, name='photo_delete'),
    path('photo_history',views.photo_history,name='photo_history'),
    path('restore/<int:pid>', views.restore, name='restore'),
    path('permanent/<int:pid>',views.permanent,name='permanent'),
     path('photos/<int:pk>/', views.photo_detail, name='photo_detail'),

]
