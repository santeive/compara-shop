from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import sqlite3


# Create your views here.
def claroshop(request):
    with sqlite3.connect("stores.sqlite3") as conn:
        cursorObj = conn.cursor()
        
        #Products
        cursorObj.execute('SELECT count(id) FROM linio')
        products = cursorObj.fetchone()

        #Brands
        cursorObj.execute('SELECT count(DISTINCT brand) FROM linio')
        brands = cursorObj.fetchone()

        #Categories
        cursorObj.execute('SELECT COUNT(DISTINCT category) FROM linio')
        rows = cursorObj.fetchone()

        context = {
            'categories': rows[0],
            'products': products[0],
            'brands': brands[0]
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