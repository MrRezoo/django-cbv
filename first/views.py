from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from first.models import Todo


class Home(ListView):
    # template_name = 'first/home.html'  # first/todo_list.html
    # queryset = Todo.objects.all() # object_list
    # model = Todo
    context_object_name = 'todos'
    ordering = ['-created']

    def get_queryset(self):
        return Todo.objects.all()


# class Home(TemplateView):
#     template_name = 'first/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['todos'] = Todo.objects.all()
#         return context

# class Home(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'first/home.html', {'name': 'mr.rezoo'})

# def home(request):
#     return render(request, 'first/home.html')


class DetailTodo(DetailView):  # AppName/ModelName_detail.html
    # model = Todo
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'

    def get_queryset(self, **kwargs):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['myslug'])
        else:
            return Todo.objects.none()
