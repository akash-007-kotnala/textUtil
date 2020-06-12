
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    # '' means kya render karna hai.. ,  views.index means index function ko call karna hai.. ,  name matlab kisnam se render karna hai link ko..
    path('analyze',views.analyze, name='analyze')
  
]
