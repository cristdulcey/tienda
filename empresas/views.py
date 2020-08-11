from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, ListView

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

        #print(search)
        if category:
            query = query.filter(category__id=category)
        if search:
            query = query.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            ).distinct()
        return query



class Test2View(TemplateView):
    template_name = 'checkout.html'

"""   def get_context_data(self, **kwargs):
        context=super(TestView, self).get_context_data(**kwargs)
        saludo='Hola mundo'
        context['mensaje']=saludo
        return context

    def saludo(self):
        ahora = timezone.now().astimezone()
        if ahora.hour < 12:
            return "Buenos dias, la hora es {}:{}".format(ahora.hour, ahora.minute)
        elif ahora.hour < 18:
            return "Buenas tardes, la hora es {}:{}".format(ahora.hour, ahora.minute)
        else:
            return "Buenas noches, la hora es {}:{}".format(ahora.hour, ahora.minute)   """


