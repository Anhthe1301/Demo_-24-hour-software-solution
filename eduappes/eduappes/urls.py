"""
URL configuration for eduappes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#nhớ import re_path và include xong rồi qua models sửa của thằng bảng mình muốn
#cài cái này thành RichTextField
from django.contrib import admin
from django.urls import path,re_path,include
#Them vao de link voi urls cua app



urlpatterns = [
    path('admin/', admin.site.urls),
    # Them dong nay de link HTML
    path('', include('edues.urls')),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
# python manage.py createsuperuser
# theanh1301
# tta1301
# -> nó sẽ tạo ra bảng edu_user dưới csdl
