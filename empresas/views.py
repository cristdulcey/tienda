from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes, api_view

from compras.models import Order, OrderProduct
from empresas.models import Client
from productos.models import Product, Category


class HomeView(ListView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data(**kwargs)
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')


        context['category']= Category.objects.all()
        context['cat']= category
        context['sea']= search


        return context


    def get_queryset(self):
        query=super(HomeView, self).get_queryset()
        category= self.request.GET.get('category')
        search = self.request.GET.get('search')


        #print(comprar)
        if category:
            query = query.filter(category__id=category)

        if search:
            query = query.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            ).distinct()
        return query




class Details(DetailView):
    template_name = 'detalles.html'
    model = Product

class Test2View(DetailView):
    template_name = 'compra.html'
    model = Product

@csrf_exempt
@api_view(['POST'])
@authentication_classes([BasicAuthentication,])
def add_product_cart_view(request,format=None):
    pk = request.POST.get("id_product")
    quantity = request.POST.get("quantity",1)
    print(pk,quantity)
    product = get_object_or_404(Product,id=pk)
    if request.user.is_authenticated:
        client = Client.objects.filter(user=request.user)
        if client: # si existe el cliente
            order = Order.objects.filter(client=client.first(), state=False) # buscar una orden con ese cliente y que no este terminada
            if order: # si existe la orden del cliente y que no este terminada
                order_aux = order.first() # asignamos a order_aux el primer elemento del array de order
                order_product, create = OrderProduct.objects.get_or_create( # busca si existe un OrderProduct con esa orden y con ese producto
                    order=order_aux,
                    product=product,
                    defaults={ # si no existe se crea con estas opciones por defecto
                        "quantity": quantity,
                        "value_unit": product.value,
                        "value_total": (product.value * quantity)
                    }
                )
                if not create:
                    # si no se crea el objeto OrderProduct entra aqui
                    order_product.quantity = int(quantity)
                    order_product.value_unit = int(product.value)
                    order_product.value_total = int(int(product.value) * int(quantity))
                    order_product.save() # guardamos las modificaciones.
                    return JsonResponse({
                        'msg': 'the product has been updated to your cart',
                        'items': pk
                    })
                else:
                    return JsonResponse({
                        'msg': 'the product has been added to your cart',
                        'items': pk
                    })
            else:

                order_aux = Order.objects.create(client=client.first(),state=False,value=0)
                order_product = OrderProduct.objects.create(
                    order=order_aux,
                    product=product,
                    quantity=quantity,
                    value_unit=product.value,
                    value_total=(product.value * quantity)
                )
                return JsonResponse({
                    'msg': 'the product has been added to your cart',
                    'items': pk
                })
    else:
        return JsonResponse({
            'msg': 'No existe el cliente',
            'items': pk
        })



"""  
 class ShoppingCart(CreateView):
    model = Product
    template_name = "compra.html"
    success_url = reverse_lazy("index.html")
 
 
 def get_context_data(self, **kwargs):
        context=super(TestView, self).get_context_data(**kwargs)
        saludo='Hola mundo'
        context['mensaje']=saludo
        return context

def saludo():
    ahora = timezone.now().astimezone()
    if ahora.hour < 12:
        return "Buenos dias, la hora es {}:{}".format(ahora.hour, ahora.minute)
    elif ahora.hour < 18:
        return "Buenas tardes, la hora es {}:{}".format(ahora.hour, ahora.minute)
    else:
        return "Buenas noches, la hora es {}:{}".format(ahora.hour, ahora.minute)
"""

