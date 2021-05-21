from django.urls import path
from . import views

urlpatterns = [
    path('hello2',views.hello2),
    path('register2/',views.register2),
    path('privacy/',views.privacy,name='privacy'),
    path('alldata2/',views.alldata2),
    path('update2/<name>',views.update2,name='update'),
    path('delete/<name>',views.delete,name='delete')
]