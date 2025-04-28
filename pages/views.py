from django.shortcuts import render
from .models import Page
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/pages_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages:pages_list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages:pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:pages_list')