from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    PATH: /
    Shows the landing page.
    If the user is currently logged in, redirect to the user status page.  PATH: /users/userid
    :param request:
    :return:
    """
    parameters = dict(
        name="Aamer",
        last_name="Rial",

    )

    return render(request, "index.html", parameters)


def login(request):
    return HttpResponse("LOGIN STUB")


def register(request):
    return HttpResponse("REGISTER STUB")


def user_detail(request, pk_user=None):
    return HttpResponse("USER DETAIL STUB USER ID: " + str(pk_user))


def groups(request):
    return HttpResponse("GROUPS STUB")


def group_detail(request, pk_group=None):
    return HttpResponse("GROUP DETAIL STUB Group ID: "+ str(pk_group))


def test(request):
    return HttpResponse("TEST REQUEST: " + str(request.path))
