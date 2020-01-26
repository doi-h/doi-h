from django.urls import path
from .views import show,edit,update, delete,new,create,test

app_name="appname"
urlpatterns = [
    path('show/<int:idd>/', show, name="show"),
    path('edit/<int:idd>/', edit, name="edit"),
    path('update/<int:idd>/', update, name="update"),
    path('delete/<int:idd>/', delete, name="delete"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('test/', test, name="test"),
]
