from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello),
    path('first_html/',views.first1_html),
    path('register/',views.register),
    path('alldata/',views.alldata),
    path('single_data/<name>',views.singledata,name = 'singledata'),
    path('update/<name>',views.update,name='updatedata'),
    path('delete/<name>',views.delete,name='delete')
]