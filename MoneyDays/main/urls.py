"""MoneyDays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login_req, name='login'),
    url(r'^logout', views.logout_req,),
    url(r'^register$', views.register),
    url(r'^users/(?P<pk_user>[0-9]+)$', views.user_detail, name='user_detail'),
    url(r'^groups$', views.groups),
    url(r'^groups/(?P<pk_group>[0-9]+)$', views.group_detail),

    url(r'^test$', views.test),
]
