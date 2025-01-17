from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'fourth_task/masloDzen.html')

def price(request):
    context  = {
        'price': ['Подсолнечное масло (250 мл.) - 280 руб.',
          'Льняное масло (250 мл.) - 310 руб.',
          'Масло грецкого ореха (250 мл.) - 750 руб.',
          'Масло конопляного семени (250 мл.) - 950 руб.']
    }
    return render(request, 'fourth_task/prices_maslo.html', context)

def disc(request):
    return render(request, 'fourth_task/description_maslo.html')

