from basicauth.decorators import basic_auth_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from compras.models import Order
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

#@basic_auth_required
@csrf_exempt
def add_product_cart_view(request):
    pk = request.POST.get("id_product")
    print(request.user)
    if request.user.is_authenticated:

        client = Client.objects.filter(user=request.user)
        print(client)

        if client:
            order = Order.objects.filter(client = client, state=False)
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

