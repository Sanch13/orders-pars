from datetime import date
from django.shortcuts import render

from ordlist.forms import PriceForm
from ordlist.models import DataIcetrade, DataGoszakupki


def index(request):
    form = PriceForm(data=request.GET)
    if form.is_valid():
        min_price = 1 if form.cleaned_data.get("min_price") is None else form.cleaned_data.get("min_price")
        max_price = 100_000_000 if form.cleaned_data.get("max_price") is None else \
            form.cleaned_data.get("max_price")
        context = sort_price(min_price=int(min_price), max_price=int(max_price))
        context['form'] = PriceForm()
        return render(request, "ordlist/base.html", context=context)


def sort_price(day=date.today(), min_price=1, max_price=100_000_000):
    total_today_ice = DataIcetrade.objects.filter(date=day,
                                                  price__gte=min_price,
                                                  price__lte=max_price).count()
    total_today_gos = DataGoszakupki.objects.filter(date=day,
                                                    price__gte=min_price,
                                                    price__lte=max_price).count()
    orders_ice = DataIcetrade.objects.filter(date=day,
                                             price__gte=min_price,
                                             price__lte=max_price)
    orders_gos = DataGoszakupki.objects.filter(date=day,
                                               price__gte=min_price,
                                               price__lte=max_price)
    context = {
        "orders_ice": orders_ice,
        "orders_gos": orders_gos,
        "total_today_ice": total_today_ice,
        "total_today_gos": total_today_gos
    }
    return context
