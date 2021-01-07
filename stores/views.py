from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import sqlite3


# Create your views here.
def claroshop(request):
    with sqlite3.connect("stores.sqlite3") as conn:
        cursorObj = conn.cursor()
        
        #Products
        cursorObj.execute('SELECT count(id) FROM claro')
        products = cursorObj.fetchone()

        #Brands
        cursorObj.execute('SELECT count(DISTINCT brand) FROM claro')
        brands = cursorObj.fetchone()

        #Categories
        cursorObj.execute('SELECT COUNT(DISTINCT category) FROM claro')
        rows = cursorObj.fetchone()

        #STOCK
        cursorObj.execute('SELECT COUNT(stock) FROM claropriceproducts WHERE stock > 0')
        stock_av = cursorObj.fetchone()

        context = {
            'categories': rows[0],
            'products': products[0],
            'brands': brands[0],
            'stock_av': stock_av[0],
        }
        return render(request, 'stores/claroshop.html', context)

def linio(request):
    with sqlite3.connect("stores.sqlite3") as conn:
        cursorObj = conn.cursor()
        
        #Products
        cursorObj.execute('SELECT count(sku) FROM claro')
        products = cursorObj.fetchone()

        #Brands
        cursorObj.execute('SELECT count(DISTINCT brand) FROM claro')
        brands = cursorObj.fetchone()

        #Categories
        cursorObj.execute('SELECT COUNT(DISTINCT category) FROM claro')
        rows = cursorObj.fetchone()

        context = {
            'categories': rows[0],
            'products': products[0],
            'brands': brands[0]
        }
        return render(request, 'stores/linio.html', context)

def walmart(request):
    titulo = 'Pagina base'
    context = {
        'titulo': titulo
    }
    return render(request, 'stores/walmart.html', context)