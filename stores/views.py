from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def claroshop(request):
    records = 24334
    context = {
        'records': records
    }
    return render(request, 'stores/claroshop.html', context)

def linio(request):
    titulo = 'Pagina base'
    context = {
        'titulo': titulo
    }
    return render(request, 'stores/linio.html', context)

def walmart(request):
    titulo = 'Pagina base'
    context = {
        'titulo': titulo
    }
    return render(request, 'stores/walmart.html', context)