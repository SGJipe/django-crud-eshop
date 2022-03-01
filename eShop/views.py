from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, F, Value

from .models import Pokemon
from eShop.forms import PokemonQtyForm
# Create your views here.

def catalogue(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'eShop/catalogue.html', {'pokemons': pokemon})

def product_detail(request, product_id):
    pokemon = get_object_or_404(Pokemon, pk=product_id)
    errorMsg = False
    if request.method == 'POST':
        form = PokemonQtyForm(request.POST or None)
        if form.is_valid():
                quantityBought = form.cleaned_data.get('quantity')
                if quantityBought <= pokemon.quantity:
                    pokemon.quantity -= quantityBought
                    pokemon.save()
                else:
                    return HttpResponseRedirect('/eshop/product-detail/'+ str(product_id) +'?errorMsg=True')
    else:
        form = PokemonQtyForm
        if 'errorMsg' in request.GET:
            errorMsg = True  
            # else:
            #     errorMsg = True
            #     print(pokemon.quantity)
                # return HttpResponseRedirect('/eshop/product-detail/'+ str(product_id) +'?error=True')

    form = PokemonQtyForm
    return render(request, 'eShop/product-detail.html', {'pokemon': pokemon, 'form': form, 'errorMsg': errorMsg})

# def buy_product(request, product_id):
#     pokemon = get_object_or_404(Pokemon ,pk=product_id)
#     form = PokemonQuantityForm(request.POST or None, instance=pokemon)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, 'eShop/product-detail.html', {'pokemon': pokemon, 'form': form})

def chat_socket(request):
    room_code = 1
    return redirect(
            '/eshop/chat/%s' 
            %(room_code)
        )

def chat_board(request, room_code):
    room_code = 1
    return render(request, "eShop/chat.html", {'room_code': room_code})