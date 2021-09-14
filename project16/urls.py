"""project16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_access/',display_access,name='display_access'),
    path('delete_webpage/',delete_webpage,name='delete_webpage'),
    path('update_webpage/',update_webpage,name='update_webpage'),
    path('create_topic/',create_topic,name='create_topic'),
    path('create_webpage/',create_webpage,name='create_webpage'),
    path('multi_select/',multi_select,name='multi_select'),
    path('checkbox/',checkbox,name='checkbox'),
]

admin.site.site_header='Harshad'
admin.site.site_title='Sports'
admin.site.index_title='DHONI'
