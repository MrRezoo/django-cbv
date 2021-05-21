from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView, UpdateView

from first.forms import TodoCreateForm
from first.models import Todo


class Home(ListView):
    # template_name = 'first/home.html'  # default => first/todo_list.html
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


# class TodoCreate(FormView):
#     template_name = 'first/todo_create.html'
#     form_class = TodoCreateForm
#     success_url = reverse_lazy('first:home')
#     # success_url = '/create/'
#
#     def form_valid(self, form):
#         self.create_todo(form.cleaned_data)
#         return super().form_valid(form)
#
#     def create_todo(self, data):
#         todo = Todo(title=data['title'], slug=slugify(data['title']))
#         todo.save()
#         messages.success(self.request, 'your todo added', 'success')


class TodoCreate(CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo added', 'success')
        return super().form_valid(form)


class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'first/todo_delete.html'
    success_url = reverse_lazy('first:home')


class UpdateTodo(UpdateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/todo_update.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        return super().form_valid(form)


