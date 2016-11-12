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
from django.conf.urls import url, include

from . import views, apiviews

urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^login$', views.login_req, name='login'),
    # url(r'^logout', views.logout_req, ),
    # url(r'^register$', views.register),
    # url(r'^savenow$', views.make_payment),
    # url(r'^users/(?P<pk_user>[0-9]+)$', views.user_detail, name='user_detail'),
    # url(r'^groups$', views.groups),
    # url(r'^groups/(?P<pk_group>[0-9]+)$', views.group_detail),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^api/$', apiviews.api_root),

    url(r'^api/users/$', apiviews.UserList.as_view(), name='moneyuser-list'),
    url(r'^api/users/(?P<pk_user>[0-9]+|self)/$', apiviews.UserDetail.as_view(), name='moneyuser-detail'),
    # url(r'^api/users/(?P<pk_user>[0-9]+)/contributions/$', apiviews.UserContributions.as_view(), name='measurement-list'),
    # url(r'^api/users/(?P<pk_user>[0-9]+)/measurements/(?P<pk_measurement>[0-9]+)/$', views.UserMeasurementDetail.as_view(), name='measurement-detail'),
    # url(r'^test$', views.test),
]
