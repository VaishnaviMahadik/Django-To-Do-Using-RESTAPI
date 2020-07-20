from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index ,name='index'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
]
