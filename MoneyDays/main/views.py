from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def index(request):
    """
    PATH: /
    Shows the landing page.
    If the user is currently logged in, redirect to the user status page.  PATH: /users/userid
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return redirect(reverse('user_detail', kwargs={"pk_user": request.user.id}))
    else:
        return redirect(reverse('login'))


def login_req(request):
    if request.method == 'POST':
        # Do login.
        if "username" in request.POST and "password" in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            print("User: " + username)
            print("Password: " + password)
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(reverse('user_detail', kwargs={"pk_user": user.id}))
            else:
                print("Error!!!!")

    parameters = dict(
        app_name="Money Days!"
    )
    return render(request, "login.html", parameters)


def logout_req(request):
    print("Logout")
    logout(request)
    return redirect(reverse('login'))


def register(request):
    return HttpResponse("REGISTER STUB")


@login_required
def user_detail(request, pk_user=None):
    parameters = dict(
        name=request.user.first_name,
        last_name=request.user.last_name,
        app_name="Money Days!"
    )
    return render(request, "index.html", parameters)


@login_required
def groups(request):
    return HttpResponse("GROUPS STUB")


@login_required
def group_detail(request, pk_group=None):
    return HttpResponse("GROUP DETAIL STUB Group ID: " + str(pk_group))


def test(request):
    return HttpResponse("TEST REQUEST: " + str(request.path))
