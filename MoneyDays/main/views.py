from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from twilio.rest import TwilioRestClient
from main.models import UserContribution, UserPointMovement, UserGoal

from MoneyDays.keys import ACCOUNT_SID, AUTH_TOKEN


def truncate(f, n):
    """Truncates/pads a float f to n decimal places without rounding"""
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


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
                print("Error! Please try again.")

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
    # poolMembership = PoolMembership.objects.filter(user=request.user)[0]
    # pool = poolMembership.group

    print("User: " + request.user.first_name)
    # print("Pool Name: " + pool.name)

    contributions = UserContribution.objects.filter(user=request.user).order_by('-time')

    money_balances = []
    for cont in contributions:
        # print("Amount: " + str(cont.txn_amount))
        # print("Balance: " + str(cont.balance))
        # print("Time: " + str(cont.time))
        time = int(cont.time.timestamp() * 1000)
        money_balances.append((time, cont.balance))

    pointmovements = UserPointMovement.objects.filter(user=request.user).order_by('-time')

    point_balances = []
    for cont in pointmovements:
        # print("Amount: " + str(cont.txn_amount))
        # print("Balance: " + str(cont.balance))
        # print("Time: " + str(cont.time))
        time = int(cont.time.timestamp() * 1000)
        point_balances.append((time, cont.balance))

    total_saved = contributions[0].balance
    previous_saved = contributions[1].balance
    savings_increase = (total_saved / previous_saved) * 100

    total_points = pointmovements[0].balance
    previous_points = pointmovements[1].balance
    if previous_points:
        points_increase = (total_points / previous_points) * 100
    else:
        points_increase = 0

    # FIXME NO GOAL MAYBE
    goal = UserGoal.objects.filter(user=request.user)[0]

    parameters = dict(
        name=request.user.first_name,
        last_name=request.user.last_name,
        app_name="Money Days!",
        moneybalances=money_balances,
        pointbalances=point_balances,
        total_saved=truncate(total_saved, 2),
        total_points=total_points,
        goal_amount=goal.amount,
        goal_name=goal.name,
        goal_description=goal.description,
        recommended_amount=request.user.recommended_amount,
        savings_increase="%.2f" % round(savings_increase, 2),
        points_increase="%.2f" % round(points_increase, 2)
    )
    return render(request, "index.html", parameters)


@login_required
def make_payment(request):
    print("MAKE PAYMENT")
    if request.method != 'POST':
        return redirect(reverse('user_detail', kwargs={"pk_user": request.user.id}))

    if "amount" not in request.POST:
        return redirect(reverse('user_detail', kwargs={"pk_user": request.user.id}))

    amount = request.POST["amount"]
    # poolMembership = PoolMembership.objects.filter(user=request.user)[0]
    # pool = poolMembership.group

    contrib = UserContribution(user=request.user, txn_amount=float(amount))
    contrib.save()

    return redirect(reverse('user_detail', kwargs={"pk_user": request.user.id}))


@login_required
def groups(request):
    return HttpResponse("GROUPS STUB")


@login_required
def group_detail(request, pk_group=None):
    return HttpResponse("GROUP DETAIL STUB Group ID: " + str(pk_group))


def test(request):
    return HttpResponse("TEST REQUEST: " + str(request.path))
