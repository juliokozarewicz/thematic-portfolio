from django.shortcuts import render
from .models import Work
from django.views.generic import ListView, DetailView


def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'core/about.html'
    return render(request, template_name)

class work(ListView):
    model = Work
    template_name = 'core/work.html'
    context_object_name = 'view_work_list'

class detail_work(DetailView):
    model = Work
    template_name = 'sendmail/detail_work.html'
    context_object_name = 'view_detail_work'