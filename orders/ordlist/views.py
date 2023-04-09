from datetime import date
from django.shortcuts import render

from ordlist.models import DataIcetrade, DataGoszakupki


def index(request):
    context = sort_price()
    return render(request, "ordlist/base.html", context=context)


def sort_price(date=date.today(), price=0):
    total_today_ice = DataIcetrade.objects.filter(date=date.today()).count()
    total_today_gos = DataGoszakupki.objects.filter(date=date.today()).count()
    orders_ice = DataIcetrade.objects.filter(date=date.today(), ).values()
    orders_gos = DataGoszakupki.objects.filter(date=date.today()).values()
    context = {
        "orders_ice": orders_ice,
        "orders_gos": orders_gos,
        "total_today_ice": total_today_ice,
        "total_today_gos": total_today_gos
    }
    return context
