from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import ListView

from registeritem.forms import StockForm, ItemForm
from registeritem.models import Stock, Item


class Dashboard(ListView):
    model = Stock
    template_name = 'dashboard.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        context['computer_lap'] = Stock.objects.filter(category='Computer Laptop').count()
        context['laptop_given'] = Item.objects.filter(device__category='Computer Laptop').count()

        context['computer_desk'] = Stock.objects.filter(category='Computer Desktop').count()
        context['desktop_given'] = Item.objects.filter(device__category='Computer Desktop').count()

        context['printer'] = Stock.objects.filter(category='Printer').count()
        context['printer_given'] = Item.objects.filter(device__category='Printer').count()

        context['routers'] = Stock.objects.filter(category='4G Router').count()
        context['routers_given'] = Item.objects.filter(device__category='4G Router').count()

        context['scanners'] = Stock.objects.filter(category='Scanner').count()
        context['scanners_given'] = Item.objects.filter(device__category='Scanner').count()

        context['television'] = Stock.objects.filter(category='Television').count()
        context['television_given'] = Item.objects.filter(device__category='Television').count()

        context['decoder'] = Stock.objects.filter(category='Decoder').count()
        context['decoder_given'] = Item.objects.filter(device__category='Decoder').count()

        return context


def laptopList(request):
    available_lap = Stock.objects.filter(category='Computer Laptop')
    given_lap = Item.objects.filter(device__category='Computer Laptop')
    context = {'available_lap': available_lap, 'given_lap': given_lap}
    return render(request, 'laptop_list.html', context)



def finance(request):
    context = {}
    return render(request, "finance.html", context)


def profile(request):
    context = {}
    return render(request, "profile.html", context)


# -========View for adding stock
def createStock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, "create_stock.html", context)


# -========View for Updating stock
def updateStock(request, pk):
    data = Stock.objects.get(pk=pk)
    form = StockForm(instance=data)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('all_stock')
    context = {'form': form}
    return render(request, "update_stock.html", context)


# -========View for adding Item
def createItem(request):
    form = ItemForm(request=request)
    if request.method == 'POST':
        form = ItemForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, "create_item.html", context)


class ListAllStock(ListView):
    model = Stock
    template_name = 'all_stock.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListAllStock, self).get_context_data(**kwargs)
        context['all_stock'] = Stock.objects.all()
        context['all_stock_q'] = Stock.objects.filter(category='Computer Laptop').count()
        context['all_stock_new'] = Stock.objects.filter(category='Computer Laptop')\
                                        .exclude(availability='Given').count()
        context['all_item'] = Item.objects.all()
        # context['all_item'] = Stock.objects.values('')
        return context
