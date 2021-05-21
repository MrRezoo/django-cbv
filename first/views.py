from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import TemplateView

from first.models import Todo


class Home(TemplateView):
    template_name = 'first/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context

# class Home(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'first/home.html', {'name': 'mr.rezoo'})

# def home(request):
#     return render(request, 'first/home.html')
