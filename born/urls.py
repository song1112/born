"""Born URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from born_user.views import login, register, new_project
from born.views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'home', index),
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'register/', register),
    url(r'new_project/', new_project),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

