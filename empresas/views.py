from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'index.html'

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


