from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def show_funk(request):
    return render(request, 'funk_repr.html')

class show_class(TemplateView):
    template_name = 'class_repr.html'

