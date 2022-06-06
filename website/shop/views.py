from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import Login, SignUp


def startpage(request):
    products = Watches.objects.all()
    products1 = Phones.objects.all()
    return render(request, 'shop/startpage.html', {'products': products, 'products1': products1})


def watches(request):
    products = Watches.objects.all()
    mechanisms = WatchesMechanism.objects.all()
    return render(request, 'shop/watches.html', {'products': products, 'mechanisms': mechanisms})


def phones(request):
    products = Phones.objects.all()
    return render(request, 'shop/phones.html', {'products': products})


def purchase1(request):
    products = Watches.objects.get()
    return render(request, 'shop/purchase_watches.html', {'products': products})


def get_watches_mechanism(request, mechanism_id):
    products = Watches.objects.filter(mechanism_id=mechanism_id)
    mechanism = WatchesMechanism.objects.get(pk=mechanism_id)
    return render(request, 'shop/mechanisms.html', {'products': products, 'mechanism': mechanism})


def get_watches_company(request,company_id):
    products = Watches.objects.filter(company_id=company_id)
    company = WatchesCompany.objects.get(pk=company_id)
    return render(request, 'shop/companies.html', {'products': products, 'company': company})


def maps(request):
    return render(request, 'shop/map.html')


def o_nas(request):
    return render(request, 'shop/o_nas.html')


def offers(request):
    return render(request, 'shop/offers.html')


def get_watches_info(request, watches_id):
    watches = Watches.objects.get(pk=watches_id)
    return render(request, 'shop/watches_info.html', {'watches': watches})


def login(requset):
    if requset.method == 'POST':
        pass

    else:
        form = Login()
    return render(requset, 'shop/login.html', {'form': form})


def sign_up(requset):
    if requset.method == 'POST':
        pass
    else:
        form = SignUp()
    return render(requset, 'shop/login.html', {'form': form})
