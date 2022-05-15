from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmessage import sendTelegram


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    price_card_1 = PriceCard.objects.get(pk=1)
    price_card_2 = PriceCard.objects.get(pk=2)
    price_card_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'price_card_1': price_card_1,
                'price_card_2': price_card_2,
                'price_card_3': price_card_3,
                'price_table': price_table,
                'form': form,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        telegram_id = request.POST['telegram_id']
        element = Order(order_name=name, order_phone=phone, order_telegram_id=telegram_id)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone, tg_id=telegram_id)
        return render(request, './thanks.html', {'name': name,
                                                 'phone': phone,
                                                 'telegram_id': telegram_id})
    else:
        return render(request, './thanks.html')


def about(request):
    return render(request, './about.html')
