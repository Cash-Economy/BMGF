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
    url(r'^$', views.index),
    url(r'^login$', views.login_req, name='login'),
    url(r'^logout', views.logout_req, ),
    url(r'^register$', views.register),
    url(r'^savenow$', views.make_payment),
    url(r'^users/(?P<pk_user>[0-9]+)$', views.user_detail, name='user_detail'),
    # url(r'^groups$', views.groups),
    # url(r'^groups/(?P<pk_group>[0-9]+)$', views.group_detail),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/$', apiviews.api_root),

    url(r'^api/users/(?P<pk_user>[0-9]+)/savings$', apiviews.get_user_saving_recommendations),

    url(r'^api/users/$', apiviews.UserList.as_view(), name='moneyuser-list'),
    url(r'^api/users/(?P<pk_user>[0-9]+|self)/$', apiviews.UserDetail.as_view(), name='moneyuser-detail'),
    url(r'^api/users/(?P<pk_user>[0-9]+)/contributions/$', apiviews.UserContributionList.as_view(), name='contribution-list'),
    url(r'^api/users/(?P<pk_user>[0-9]+)/contributions/(?P<pk_contribution>[0-9]+)/$', apiviews.UserContributionDetail.as_view(), name='contribution-detail'),
    url(r'^api/users/(?P<pk_user>[0-9]+)/points/$', apiviews.UserPointMovementList.as_view(), name='point-list'),
    url(r'^api/users/(?P<pk_user>[0-9]+)/points/(?P<pk_contribution>[0-9]+)$', apiviews.UserPointMovementDetail.as_view(), name='point-detail'),
    url(r'^api/users/(?P<pk_user>[0-9]+)/goals/$', apiviews.UserGoalList.as_view(), name='goal-list'),

    # url(r'^test$', views.test),
]
