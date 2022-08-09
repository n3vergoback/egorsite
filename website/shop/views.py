from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .utils import *


def startpage(request):
    products = Watches.objects.all()
    products1 = Phones.objects.all()
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/startpage.html', {'products': products, 'products1': products1, 'city_by_ip': city_by_ip})


def watches(request):
    products = Watches.objects.all()
    mechanisms = WatchesMechanism.objects.all()
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/watches.html', {'products': products, 'mechanisms': mechanisms, 'city_by_ip': city_by_ip})


def phones(request):
    products = Phones.objects.all()
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/phones.html', {'products': products, 'city_by_ip': city_by_ip})


def purchase1(request):
    products = Watches.objects.get()
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/purchase_watches.html', {'products': products, 'city_by_ip': city_by_ip})


def get_watches_mechanism(request, mechanism_id):
    products = Watches.objects.filter(mechanism_id=mechanism_id)
    mechanism = WatchesMechanism.objects.get(pk=mechanism_id)
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/mechanisms.html', {'products': products, 'mechanism': mechanism, 'city_by_ip': city_by_ip})


def get_watches_company(request,company_id):
    products = Watches.objects.filter(company_id=company_id)
    company = WatchesCompany.objects.get(pk=company_id)
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/companies.html', {'products': products, 'company': company, 'city_by_ip': city_by_ip})


def maps(request):
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/map.html', {'city_by_ip': city_by_ip})


def o_nas(request):
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/o_nas.html', {'city_by_ip': city_by_ip})


def offers(request):
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/offers.html', {'city_by_ip': city_by_ip})


def get_watches_info(request, watches_id):
    watches = Watches.objects.get(pk=watches_id)
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/watches_info.html', {'watches': watches, 'city_by_ip': city_by_ip})


def user_register(request):
    city_by_ip = get_city_by_ip('25.138.133.148')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/sign_up.html', {'form': form, 'city_by_ip': city_by_ip})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'shop/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class SearchResultView(ListView):
    model = Watches
    template_name = 'shop/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Watches.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query))
        return object_list


def user_location(request):
    city_by_ip = get_city_by_ip('25.138.133.148')
    return render(request, 'shop/user_location.html', {'city_by_ip': city_by_ip})

