"""
URL configuration for fake_instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from .views import Sub, Sub1, Sub2, Sub3
from fake_insta.views import Main # Main 클래스 호출

urlpatterns = [
    path('admin/', admin.site.urls), # admin 실행시 뒤의 url을 실행하겠다
    path('', Main.as_view()),       # 아무것도 입력 안했을때 Main 클래스를 view로 사용하겠다(as_view).
    path('main/', Main.as_view()),  # main 입력시에도 Main 클래스를 view로 사용하겠다(as_view).
]
